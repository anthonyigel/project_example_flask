import pyspark.sql.functions as f

def my_shared_func(df,my_param):
    """
    Performs a common function across my job
    :param df: Spark dataframe to perform function on
    :type df: pyspark.sql.dataframe.DataFrame
    :param my_param: Some parameter that is relevant
    :type my_param: string
    :return df_result: Spark dataframe with function applied
    :type df_result: pyspark.sql.dataframe.DataFrame
    """
#     df_result = df.something
    return df_result
