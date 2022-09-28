from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gembased.config.ConfigStore import *
from gembased.udfs.UDFs import *

def Make_URLs(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(
            lit("https://api.instantwebtools.net/v2/passenger?page="), 
            col("id").cast(IntegerType()), 
            lit("&size=10&startDate="), 
            date_sub(current_date(), 1)
          )\
          .alias("url")
    )
