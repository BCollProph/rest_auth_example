from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gembased.config.ConfigStore import *
from gembased.udfs.UDFs import *

def MakeHeaders(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        to_json(expr("named_struct('Authorization', concat('Bearer ', content_parsed.access_token))")).alias("headers")
    )
