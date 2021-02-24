import pyspark.sql.functions as f

def my_func(spark,file_path):
    """
    Example function
    :param spark: Active spark session
    :type df: pyspark.sql.session.SparkSession
    :param file_path: Bucket location of file to read
    :type round_cols: string
    :return df: Spark dataframe of interest
    :type df: pyspark.sql.dataframe.DataFrame
    """
    return spark.read.parquet(file_path)\
                .filter(f.col('SOME_COL')=='FILTER_VALUE')
