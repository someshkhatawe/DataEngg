from pyspark.sql import SparkSession
import pyspark.sql.functions  as f
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

