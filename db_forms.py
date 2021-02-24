from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, FloatField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, NumberRange, Email
from flask_wtf.file import FileField, FileAllowed, FileRequired


###############################################################################
# Forms
###############################################################################
#####################################
# Edit Demand Group
#####################################
class EditDGForm(FlaskForm):
    dg_id = StringField('id')
    dg_stage = StringField('stage')
    dg_pid_fyt_pmy_dpt_cd = StringField('pid_fyt_pmy_dpt_cd')
    dg_pid_fyt_pmy_dpt_dsc_tx = StringField('pid_fyt_pmy_dpt_dsc_tx')
    dg_pid_fyt_rec_dpt_cd = StringField('pid_fyt_rec_dpt_cd')
    dg_pid_fyt_rec_dpt_dsc_tx = StringField('pid_fyt_rec_dpt_dsc_tx')
    dg_pid_fyt_sub_dpt_cd = StringField('pid_fyt_sub_dpt_cd')
    dg_pid_fyt_sub_dpt_dsc_tx = StringField('pid_fyt_sub_dpt_dsc_tx')
    dg_pid_fyt_com_cd = StringField('pid_fyt_com_cd')
    dg_pid_fyt_com_dsc_tx = StringField('pid_fyt_com_dsc_tx')
    dg_pid_fyt_sub_com_cd = StringField('pid_fyt_sub_com_cd')
    dg_pid_fyt_sub_com_dsc_tx = StringField('pid_fyt_sub_com_dsc_tx')
    dg_demand_group_code = StringField('demand_group_code', validators=[DataRequired()])
    dg_demand_group_dsc = TextAreaField('demand_group_dsc', validators=[DataRequired()])
    dg_cycle_date = StringField('cycle_date')
    submit = SubmitField('Submit')


#####################################
# Add Demand Group
#####################################
class AddDGForm(FlaskForm):
    dg_demand_group_code = StringField('demand_group_code', validators=[DataRequired()])
    dg_demand_group_dsc = TextAreaField('demand_group_dsc', validators=[DataRequired()])
    submit = SubmitField('Submit')
