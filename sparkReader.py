from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder.appName('ProjectPro').getOrCreate()


df = spark.read.format("csv").option("header", "true").option("inferSchema","true").load("F:/dataset/")

df.printSchema()

df.show()