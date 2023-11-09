from pyspark.sql import SparkSession
import pyspark.sql.functions  as f
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

df = spark.read.format("csv").option("headers", "true").load("F:/Trendy tech/week 12/1.Dataset/dataset1")

df1 = df.toDF("name", "age", "city")

def ageCheck(age, city):
    if int(age) >18:
        return str("Y" + city)
    else:
        return str("N" + city)

parseAgeFunction = f.udf(lambda x,y : ageCheck(x,y),StringType())

# df2 = df.withColumn("adult",parseAgeFunction("age") )


df2 = df1.withColumn("adult",parseAgeFunction("age","city") )

df2.printSchema()

df2.show()



