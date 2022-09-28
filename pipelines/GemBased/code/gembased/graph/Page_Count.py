from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gembased.config.ConfigStore import *
from gembased.udfs.UDFs import *

def Page_Count(spark: SparkSession) -> DataFrame:
    out0 = spark.range(Config.PAGE_COUNT)

    return out0
