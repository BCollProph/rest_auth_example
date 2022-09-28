from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gembased.config.ConfigStore import *
from gembased.udfs.UDFs import *

def URLS_Auth(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (lit(1) == lit(1)), "inner")\
        .select(col("in1.url").alias("url"), col("in0.headers").alias("headers"))
