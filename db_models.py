import pandas as pd

# Solution resources
from resources.config import parameters, create_sol_config, paths, option_3_files

sol_config = create_sol_config(paths=paths, files=option_3_files)
sol_config["parameters"] ={}
sol_config["parameters"] = parameters

# Databse
import sqlite3
from configparser import ConfigParser


###############################################################
# Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

###############################################################
# Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dg_records.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect to Database
db = SQLAlchemy(app)
con = sqlite3.connect('dg_records.db', check_same_thread=False)

###############################################################

class DG_all(db.Model):
    """
    Purpose: Table structures to be used by the Demand Group app..
    Use: Contains the tabulator_test definitions for DG records

    """
    __tablename__ = "all_dg_records"
    __table_args__ = {'extend_existing': True}
    """
    Purpose: Table structures to be used by the DG app..
    Use: Contains the table definitions for preprocessed Demand Group records


        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage = db.Column(db.String(10), nullable=False)
    pid_fyt_pmy_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_pmy_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_rec_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_rec_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_sub_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_com_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_com_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_com_cd = db.Column(db.String(5), nullable=True)
    pid_fyt_sub_com_dsc_tx = db.Column(db.String(80), nullable=True)
    demand_group_code = db.Column(db.String, nullable=True)
    demand_group_dsc = db.Column(db.String(80), nullable=True)
    cycle_date = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f'{self.id, self.stage, self.pid_fyt_pmy_dpt_cd, self.pid_fyt_pmy_dpt_dsc_tx, self.pid_fyt_rec_dpt_cd, self.pid_fyt_rec_dpt_dsc_tx, self.pid_fyt_sub_dpt_cd, self.pid_fyt_sub_dpt_dsc_tx, self.pid_fyt_com_cd, self.pid_fyt_com_dsc_tx, self.pid_fyt_sub_com_cd, self.pid_fyt_sub_com_dsc_tx, self.demand_group_code, self.demand_group_dsc, self.cycle_date}'


###############################################################


class DG_unchanged(db.Model):
    """
    Purpose: Table structures to be used by the Demand Group app..
    Use: Contains the tabulator_test definitions for DG records

    """
    __tablename__ = "unchanged_dg_records"
    __table_args__ = {'extend_existing': True}
    """
    Purpose: Table structures to be used by the DG app..
    Use: Contains the table definitions for preprocessed Demand Group records


        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage = db.Column(db.String(10), nullable=False)
    pid_fyt_pmy_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_pmy_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_rec_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_rec_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_sub_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_com_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_com_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_com_cd = db.Column(db.String(5), nullable=True)
    pid_fyt_sub_com_dsc_tx = db.Column(db.String(80), nullable=True)
    demand_group_code = db.Column(db.String, nullable=True)
    demand_group_dsc = db.Column(db.String(80), nullable=True)
    cycle_date = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f'{self.id, self.stage, self.pid_fyt_pmy_dpt_cd, self.pid_fyt_pmy_dpt_dsc_tx, self.pid_fyt_rec_dpt_cd, self.pid_fyt_rec_dpt_dsc_tx, self.pid_fyt_sub_dpt_cd, self.pid_fyt_sub_dpt_dsc_tx, self.pid_fyt_com_cd, self.pid_fyt_com_dsc_tx, self.pid_fyt_sub_com_cd, self.pid_fyt_sub_com_dsc_tx, self.demand_group_code, self.demand_group_dsc, self.cycle_date}'


###############################################################


class DG_new(db.Model):
    """
    Purpose: Table structures to be used by the Demand Group app..
    Use: Contains the tabulator_test definitions for DG records

    """
    __tablename__ = "new_dg_records"
    __table_args__ = {'extend_existing': True}
    """
    Purpose: Table structures to be used by the DG app..
    Use: Contains the table definitions for preprocessed Demand Group records


        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage = db.Column(db.String(10), nullable=False)
    pid_fyt_pmy_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_pmy_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_rec_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_rec_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_sub_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_com_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_com_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_com_cd = db.Column(db.String(5), nullable=True)
    pid_fyt_sub_com_dsc_tx = db.Column(db.String(80), nullable=True)
    demand_group_code = db.Column(db.String, nullable=True)
    demand_group_dsc = db.Column(db.String(80), nullable=True)
    cycle_date = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f'{self.id, self.stage, self.pid_fyt_pmy_dpt_cd, self.pid_fyt_pmy_dpt_dsc_tx, self.pid_fyt_rec_dpt_cd, self.pid_fyt_rec_dpt_dsc_tx, self.pid_fyt_sub_dpt_cd, self.pid_fyt_sub_dpt_dsc_tx, self.pid_fyt_com_cd, self.pid_fyt_com_dsc_tx, self.pid_fyt_sub_com_cd, self.pid_fyt_sub_com_dsc_tx, self.demand_group_code, self.demand_group_dsc, self.cycle_date}'



###############################################################


class DG_old(db.Model):
    """
    Purpose: Table structures to be used by the Demand Group app..
    Use: Contains the tabulator_test definitions for DG records

    """
    __tablename__ = "old_dg_records"
    __table_args__ = {'extend_existing': True}
    """
    Purpose: Table structures to be used by the DG app..
    Use: Contains the table definitions for preprocessed Demand Group records


        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage = db.Column(db.String(10), nullable=False)
    pid_fyt_pmy_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_pmy_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_rec_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_rec_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_sub_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_com_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_com_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_com_cd = db.Column(db.String(5), nullable=True)
    pid_fyt_sub_com_dsc_tx = db.Column(db.String(80), nullable=True)
    demand_group_code = db.Column(db.String, nullable=True)
    demand_group_dsc = db.Column(db.String(80), nullable=True)
    cycle_date = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f'{self.id, self.stage, self.pid_fyt_pmy_dpt_cd, self.pid_fyt_pmy_dpt_dsc_tx, self.pid_fyt_rec_dpt_cd, self.pid_fyt_rec_dpt_dsc_tx, self.pid_fyt_sub_dpt_cd, self.pid_fyt_sub_dpt_dsc_tx, self.pid_fyt_com_cd, self.pid_fyt_com_dsc_tx, self.pid_fyt_sub_com_cd, self.pid_fyt_sub_com_dsc_tx, self.demand_group_code, self.demand_group_dsc, self.cycle_date}'


###############################################################
class DG_updated(db.Model):
    """
    Purpose: Table structures to be used by the Demand Group app..
    Use: Contains the tabulator_test definitions for DG records

    """
    __tablename__ = "updated_dg_records"
    __table_args__ = {'extend_existing': True}
    """
    Purpose: Table structures to be used by the DG app..
    Use: Contains the table definitions for preprocessed Demand Group records


        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stage = db.Column(db.String(10), nullable=False)
    pid_fyt_pmy_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_pmy_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_rec_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_rec_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_dpt_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_sub_dpt_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_com_cd = db.Column(db.String(3), nullable=False)
    pid_fyt_com_dsc_tx = db.Column(db.String(80), nullable=False)
    pid_fyt_sub_com_cd = db.Column(db.String(5), nullable=True)
    pid_fyt_sub_com_dsc_tx = db.Column(db.String(80), nullable=True)
    demand_group_code = db.Column(db.String, nullable=True)
    demand_group_dsc = db.Column(db.String(80), nullable=True)
    cycle_date = db.Column(db.String(6), nullable=False)

    def __repr__(self):
        return f'{self.id, self.stage, self.pid_fyt_pmy_dpt_cd, self.pid_fyt_pmy_dpt_dsc_tx, self.pid_fyt_rec_dpt_cd, self.pid_fyt_rec_dpt_dsc_tx, self.pid_fyt_sub_dpt_cd, self.pid_fyt_sub_dpt_dsc_tx, self.pid_fyt_com_cd, self.pid_fyt_com_dsc_tx, self.pid_fyt_sub_com_cd, self.pid_fyt_sub_com_dsc_tx, self.demand_group_code, self.demand_group_dsc, self.cycle_date}'

###############################################################


def load_database(_DGtable, _dbTable):

    db.session.query(_dbTable).delete()
    db.session.commit()

    # Populate the database table
    for _index, _row in _DGtable.iterrows():
        # Each element in the list is an attribute for the tabulator_test class
        # Iterating through rows and inserting into tabulator_test
        DG_row = _dbTable(id=_row[0],
                      stage=_row[1],
                      pid_fyt_pmy_dpt_cd=_row[2],
                      pid_fyt_pmy_dpt_dsc_tx=_row[3],
                      pid_fyt_rec_dpt_cd=_row[4],
                      pid_fyt_rec_dpt_dsc_tx=_row[5],
                      pid_fyt_sub_dpt_cd=_row[6],
                      pid_fyt_sub_dpt_dsc_tx=_row[7],
                      pid_fyt_com_cd=_row[8],
                      pid_fyt_com_dsc_tx=_row[9],
                      pid_fyt_sub_com_cd=_row[10],
                      pid_fyt_sub_com_dsc_tx=_row[11],
                      demand_group_code=_row[12],
                      demand_group_dsc=_row[13],
                      cycle_date=_row[14])

        db.session.add(DG_row)
    db.session.commit()


###############################################################

def reload():

    # fake = Factory.create()

    ## Reload tables
    db.drop_all()
    db.create_all()

###############################################################

def initialize_db():
    """
    Initialize database for Demand Group assignment

    :return:
    """
    ## Reload tables
    reload()

    _env = sol_config["parameters"]["env"]
    if _env == "local":
        _filepath = str(sol_config[_env]["inputs"]["unedited_parquets"]) + "\\current"
    else:
        _filepath = "gs://e451_epp_stg_0744/demand_groups/preprocessed/current"


    # Import unedited Demand Groups
    all_dg_records = pd.read_parquet(_filepath).fillna("N/A").sort_values(by=['pid_fyt_com_cd', 'pid_fyt_sub_com_cd'])


    #######################################
    # Unchanged Demand Groups
    unchanged_dg_records = all_dg_records[all_dg_records['stage'].isin(['existing', 'updated'])]

    # Orphan Demand Groups
    orphan_dg_records = all_dg_records[all_dg_records['stage'].isin(['orphan'])]

    # Orphan Demand Groups
    old_dg_records = all_dg_records[all_dg_records['stage'].isin(['expired'])]


    #######################################
    # Load data to database (dg_records.db, all_dg_records)
    load_database(all_dg_records, DG_all)

    # Load data to database (dg_records.db, unchanged_dg_records)
    load_database(unchanged_dg_records, DG_unchanged)

    # Load data to database (dg_records.db, new_dg_records)
    load_database(orphan_dg_records, DG_new)

    # Load data to database (dg_records.db, unchanged_dg_records)
    load_database(old_dg_records, DG_old)


###############################################################

def update_dg_records(target_id, target_stage, target_code, target_dsc, tbl):
    """
    Function designed to update Demand Group record in DG_all database table
    :param target_id: Record ID of target row
    :param target_stage: New stage of target row
    :param target_code: New Demand Group Code of target row
    :param target_dsc: New Demand Group Description of target row
    :param tbl: Database table name
    :return:
    """
    try:
        value = tbl.query.filter(tbl.id == int(target_id)).first()
        value.stage = str(target_stage)
        value.demand_group_code = str(target_code)
        value.demand_group_dsc = str(target_dsc)
        db.session.flush()
        db.session.commit()
        #db.session.close()
    except:
        print('Error in updating records')


###############################################################

class Config(object):
    """
    Class for reading and writing the config.yml file
    Author: Mike Ulloa 2020/04/16
    Sogeti Consultant
    """
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        self.config = ConfigParser()
        self.config.read(self.config_file)
        self.parser = ConfigParser()
        self.config.read(config_file)

    def get_key(self, section, key):
        key_value = self.config.get(section, key)
        print(key_value)
        return(key_value)

    def get_all(self):
        config = self.config
        sections_dict = {}
        for section in config.sections():
            options = config.options(section)
            temp_dict = {}
            for option in options:
                temp_dict[option] = config.get(section, option)

            sections_dict[section] = temp_dict
        return sections_dict

    def write_key(self, section, key, value):
        parser = self.parser
        parser.read(self.config_file)

        if not parser.has_section(section):
            parser.add_section(section)

        parser.set(section, key, value)
        with open(self.config_file, 'w') as configFile:
            parser.write(configFile)
