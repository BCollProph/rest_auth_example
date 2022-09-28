from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gembased.config.ConfigStore import *
from gembased.udfs.UDFs import *

def Ignore_Errors(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("api_output.status_code") == lit("200")))
