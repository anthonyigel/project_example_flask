import pandas as pd
from flask import  json


###############################################################################
## QA initial user input
def qa_user_input_record(parent_df, target_df, target_code, target_description):
    target_df['demand_group_code'] = str(target_df['demand_group_code'])
    parent_df['demand_group_code'] = str(parent_df['demand_group_code'])


    ## Determine if the Commodity | Sub-Commodity relationship already exists in the unchanged Demand Groups
    qa_check_1_df = pd.merge(parent_df, target_df, how='inner',
                             left_on=['pid_fyt_com_cd', 'pid_fyt_sub_com_cd'],
                             right_on=['pid_fyt_com_cd', 'pid_fyt_sub_com_cd'])
    if qa_check_1_df.empty:
        qa_check_1_result = "Passed QA check 1"
    else:
        qa_check_1_result = "Error"


    ## Determine if the user entered Demand Group Code already exists
    if parent_df[parent_df['demand_group_code'].isin([target_code])].empty:
        qa_check_2_result = "Passed QA check 2"

    else:
        existing_dg_record = pd.merge(parent_df, target_df, how='inner',
                             left_on=['demand_group_code'],
                             right_on=['demand_group_code'])
        if existing_dg_record['demand_group_description'] == target_description:
            qa_check_2_result = "Passed QA check 2"
        else:
            qa_check_2_result = "Error"

    if qa_check_1_result == "Error" or qa_check_2_result == "Error":
        qa_message = "Error"
    else:
        qa_message = "Success"

    return qa_message
