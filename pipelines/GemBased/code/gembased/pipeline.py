from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from gembased.config.ConfigStore import *
from gembased.udfs.UDFs import *
from prophecy.utils import *
from gembased.graph import *

def pipeline(spark: SparkSession) -> None:
    df_DummyInput1 = DummyInput1(spark)
    df_RestAPIEnrich_0 = RestAPIEnrich_0(spark, df_DummyInput1)
    df_MakeHeaders = MakeHeaders(spark, df_RestAPIEnrich_0)
    df_Page_Count = Page_Count(spark)
    df_Make_URLs = Make_URLs(spark, df_Page_Count)
    df_URLS_Auth = URLS_Auth(spark, df_MakeHeaders, df_Make_URLs)
    df_API_Call = API_Call(spark, df_URLS_Auth)
    df_Ignore_Errors = Ignore_Errors(spark, df_API_Call)
    df_Make_URLs_With_Date = Make_URLs_With_Date(spark, df_Page_Count)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "3422/pipelines/GemBased")
    MetricsCollector.start(spark = spark, pipelineId = "3422/pipelines/GemBased")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
