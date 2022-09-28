from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gembased.config.ConfigStore import *
from gembased.udfs.UDFs import *

def RestAPIEnrich_0(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from prophecy.udfs import get_rest_api
    requestDF = in0.withColumn(
        "api_output",
        get_rest_api(
          to_json(
            struct(
              lit("POST").alias("method"), 
              lit("https://dev-457931.okta.com/oauth2/aushd4c95QtFHsfWt4x6/v1/token").alias("url"), 
              lit(
                  f"scope=offline_access&grant_type=password&username={Config.API_USERNAME}&password={Config.API_PASSWORD}&client_id={Config.API_CLIENT_ID}"
                )\
                .alias("data"), 
              lit("{\"Content-Type\": \"application/x-www-form-urlencoded\"}").alias("headers")
            )
          ),
          lit("")
        )
    )

    return requestDF.withColumn(
        "content_parsed",
        from_json(col("api_output.content"), schema_of_json(requestDF.select("api_output.content").take(1)[0][0]))
    )
