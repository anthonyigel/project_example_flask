import json
import os
import sqlite3

import pandas as pd
from flask import Flask, render_template, flash, request, redirect, Blueprint, json
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flaskext.markdown import Markdown
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import utility

# Solution resources
from db_forms import AddDGForm
from db_models import DG_all, initialize_db, update_dg_records
from flask_functions import qa_user_input_record


###############################################################
# Solution Config settings
from resources.config import parameters, create_sol_config, paths, option_3_files

sol_config = create_sol_config(paths=paths, files=option_3_files)
sol_config["parameters"] = {}
sol_config["parameters"] = parameters

###############################################################
# Flask
app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = 'my secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dg_records.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['DEBUG'] = False

###############################################################
# Import Config class and assign sqlite engine
config = utility.Config()
engine = create_engine("sqlite:///dg_records.db")  # Creating the engine

# Initialize database using SQLAlchemy, specifying app is argument
db = SQLAlchemy(app)
db.init_app(app)
db.app = app

# Set app.secret_key and csrf to ensure data is encrypted when it is submitted
app.secret_key = 'Not so helpful when your code is on GitHub'
bootstrap = Bootstrap(app)
csrf = CSRFProtect(app)
moment = Moment(app)
md = Markdown(app)

# Set pandas to show all text in html renderings of DataFrames.
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

###############################################################
# Initialize Database
initialize_db()

# Create a string variable to query records from database
query_all_records = "SELECT * FROM all_dg_records"  # String containing the SQL query to select all rows from all_dg_records table
query_orphan_records = "SELECT * FROM new_dg_records"  # String containing the SQL query to select all rows from new_dg_records table
query_unchanged_records = "SELECT * FROM unchanged_dg_records"  # String containing the SQL query to select unchanged rows from all_dg_records table
query_old_records = "SELECT * FROM old_dg_records"  # String containing the SQL query to select all rows from old_dg_records table

###############################################################################
# Routes
###############################################################################

#####################################
# Home
#####################################
@app.route("/", methods=('GET', 'POST'))
def home():

    # Establish connection to database records
    con = sqlite3.connect('dg_records.db', check_same_thread=False)

    ## Assign blank form to pass through into html page
    form = AddDGForm()

    #######################################
    ## Retrieve Unchanged Demand Groups
    all_dg_records = pd.read_sql_query(query_all_records, engine)
    unchanged_dg_records = all_dg_records[all_dg_records['stage'].isin(['existing', 'updated'])]

    ## Retrieve orphan Demand Groups
    orphan_dg_records = all_dg_records[all_dg_records['stage'].isin(['orphan'])]
    orphan_dg_records = orphan_dg_records[['id', 'stage', 'pid_fyt_com_cd', 'pid_fyt_com_dsc_tx', 'pid_fyt_sub_com_cd',
                                           'pid_fyt_sub_com_dsc_tx']].sort_values(
        by=['pid_fyt_com_cd', 'pid_fyt_sub_com_cd'])

    # Ensure data is in a dataframe
    j_data = pd.DataFrame(data=orphan_dg_records)

    # Define month of current Demand Group file
    try:
        _month = orphan_dg_records.iloc[0]['cycle_date']
    except:
        _month = unchanged_dg_records.iloc[0]['cycle_date']

    ### Return HTML of homepage
    return render_template("web/gui_homepage.html", month=_month, column_names=j_data.columns.values,
                           row_data=list(j_data.values.tolist()))


#####################################
# Edit DG Record
#####################################
@app.route("/edit_demand_group/dgcode=<string:id>", methods=('GET', 'POST'))
def add_demand_group(id):
    #######################################
    ## Retrieve all Demand Groups
    all_dg_records = pd.read_sql_query(query_all_records, engine)

    ## Retrieve orphan Demand Groups
    orphan_dg_records = all_dg_records[all_dg_records['stage'].isin(['orphan'])]

    ## Retrieve Unchanged Demand Groups
    unchanged_dg_records = all_dg_records[all_dg_records['stage'].isin(['existing', 'updated'])]

    ## Retrieve old Demand Groups
    old_dg_records = all_dg_records[all_dg_records['stage'].isin(['expired'])]

    ## Parent Records
    parent_qa_records = pd.concat([unchanged_dg_records, old_dg_records])

    # Define target record to modify Demand Group
    target_id = str(id)

    # Isolate target record by ID
    target_dg_records = orphan_dg_records[orphan_dg_records['id'].isin([target_id])]
    target_dg_records['demand_group_code'] = str(target_dg_records['demand_group_code'])

    #######################################
    if request.method == 'POST':

        # Absorb form values from user
        form_code = str(request.form['DGCodeInput'])
        form_description = str(request.form['DGDscInput']).upper()
        form_id = str(target_id)

        ## QA User input
        # This checks whether or not the orphan record is already the database as well as if the Demand Group code assignment is already taken
        qa_message = qa_user_input_record(parent_df=unchanged_dg_records, target_df=target_dg_records,
                                          target_code=form_code, target_description=form_description)

        if qa_message == "Error":
            #######################################
            # Add blank form to ensure CRSF security on form submit
            form = AddDGForm()

            # Convert to JSON
            target_dg_records = target_dg_records[
                ['id', 'stage', 'pid_fyt_com_cd', 'pid_fyt_com_dsc_tx', 'pid_fyt_sub_com_cd', 'pid_fyt_sub_com_dsc_tx']]
            child_dg_records = list(target_dg_records.values.tolist())

            # Isolate Commodity Code of record
            _comm_cd = target_dg_records.iloc[0]['pid_fyt_com_cd']

            #######################################
            # Isolate Commodity Description of record
            _comm_dsc = target_dg_records.iloc[0]['pid_fyt_com_dsc_tx']

            # Combine Expired and Existing Demand Group records
            parent_old_records = old_dg_records[old_dg_records['pid_fyt_com_dsc_tx'].str.contains(_comm_dsc)]
            parent_unchanged_records = unchanged_dg_records[unchanged_dg_records['pid_fyt_com_cd'].isin([_comm_cd])]

            parent_dg_records = pd.concat([parent_old_records, parent_unchanged_records]).sort_values(
                by=['demand_group_dsc'])

            # Convert to JSON
            parent_dg_records = parent_dg_records.to_json(orient="records")
            parent_dg_records = json.dumps(json.loads(parent_dg_records), indent=2, sort_keys=True)

            #######################################
            # Determine new DG code if that is chosen
            distinct_dgs = parent_unchanged_records[['demand_group_code']].drop_duplicates(['demand_group_code'])
            distinct_dgs['demand_group_code'] = pd.to_numeric(distinct_dgs['demand_group_code'], errors='coerce')
            new_dg_code = distinct_dgs['demand_group_code'].max()
            new_dg_code = new_dg_code + 1

            flash(f'Error in user input', 'danger')
            return (render_template("web/edit_dg_record.html", child_df=child_dg_records, parent_df=parent_dg_records,
                                    dg_code_max=new_dg_code, form=form, qa=qa_message))

        else:
            # Isolate and update target Demand Group records with form inputs
            temp_records = target_dg_records
            temp_records['id'] = temp_records['id'].astype(int)
            temp_records['stage'] = 'updated'
            temp_records['demand_group_code'] = str(form_code)
            temp_records['demand_group_dsc'] = str(form_description)

            # Establish connection to database records
            con = sqlite3.connect('dg_records.db', check_same_thread=False)

            # Create a configured "Session" class
            session = sessionmaker()
            session.configure(bind=engine)

            # load_database(temp_records, DG_all)
            update_dg_records(target_id=temp_records.iloc[0]['id'],
                              target_stage=temp_records.iloc[0]['stage'],
                              target_code=temp_records.iloc[0]['demand_group_code'],
                              target_dsc=temp_records.iloc[0]['demand_group_dsc'],
                              tbl=DG_all)

            flash(f'Successfully added record to database', 'success')
            return redirect("/")

    else:

        #######################################
        # Add blank form to ensure CRSF security on form submit
        form = AddDGForm()

        # Isolate Commodity Code of record
        _comm_cd = target_dg_records.iloc[0]['pid_fyt_com_cd']

        # Convert to JSON
        target_dg_records = target_dg_records[
            ['id', 'stage', 'pid_fyt_com_cd', 'pid_fyt_com_dsc_tx', 'pid_fyt_sub_com_cd', 'pid_fyt_sub_com_dsc_tx']]
        child_dg_records = list(target_dg_records.values.tolist())

        #######################################
        # Isolate Commodity Description of record
        _comm_dsc = target_dg_records.iloc[0]['pid_fyt_com_dsc_tx']

        # Combine Expired and Existing Demand Group records
        parent_old_records = old_dg_records[old_dg_records['pid_fyt_com_dsc_tx'].str.contains(_comm_dsc)]
        parent_unchanged_records = unchanged_dg_records[unchanged_dg_records['pid_fyt_com_cd'].isin([_comm_cd])]

        parent_dg_records = pd.concat([parent_old_records, parent_unchanged_records]).sort_values(
            by=['demand_group_dsc'])

        # Convert to JSON
        parent_dg_records = parent_dg_records.to_json(orient="records")
        parent_dg_records = json.dumps(json.loads(parent_dg_records), indent=2, sort_keys=True)

        #######################################
        # Determine new DG code if that is chosen
        distinct_dgs = unchanged_dg_records[['demand_group_code']].drop_duplicates(['demand_group_code'])
        distinct_dgs['demand_group_code'] = pd.to_numeric(distinct_dgs['demand_group_code'])
        new_dg_code = distinct_dgs['demand_group_code'].max()
        new_dg_code = new_dg_code + 1

        return (render_template("web/edit_dg_record.html", child_df=child_dg_records, parent_df=parent_dg_records,
                                dg_code_max=new_dg_code, form=form))


#####################################
# Instructions
#####################################
@app.route("/instructions/")
def instructions():
    return (render_template("web/instructions.html"))


###############################################################################
# Database pages
###############################################################################
@app.route("/database_records")
def get_database_records():
    return (render_template("web/instructions.html"))


###############################################################################
# Final submit page
###############################################################################
@app.route('/upload_success')
def submit_dg_updates():
    # Establish connection to database records
    con = sqlite3.connect('dg_records.db', check_same_thread=False)

    #######################################
    ## Retrieve All Demand Groups
    all_dg_records = pd.read_sql_query(query_all_records, engine)

    ## Retrieve orphan Demand Groups
    orphan_dg_records = all_dg_records[all_dg_records['stage'].isin(['orphan'])]

    #######################################
    ## Ensure there are no more records to update
    if orphan_dg_records.empty:
        # Get current month for processing to final location
        _month = all_dg_records.iloc[0]['cycle_date']
        _env = sol_config["parameters"]["env"]

        # Subset final data
        final_submissions = all_dg_records[all_dg_records['stage'].isin(['existing', 'updated'])]

        # Save data to parquet
        output_loc_1 = sol_config[_env]["outputs"]["csa_input"] + "\\" + str(_month) + "\\cycle_date=" + str(_month)
        final_submissions.to_parquet(path=output_loc_1)

        return redirect(url_for('web/successful_upload_v1.html', month_submission=_month))
    else:
        flash(f'All records must be edited before submitting', 'info')
        return redirect("/")


###############################################################################
if __name__ == '__main__':
    app.run(port=os.getenv('SERVICE_PORT', 5000))
    db.create_all()
    app.run(debug=False, threaded=True)
    csrf.init_app(app)
