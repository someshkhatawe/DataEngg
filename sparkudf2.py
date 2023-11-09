from pyspark.sql import SparkSession
import pyspark.sql.functions  as f
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

df = spark.createDataFrame(data=data,schema=columns)

def up(x, y):

    return x.upper() + str(y)

up_udf  = f.udf(up, StringType())

# df2 = df.withColumn("Name", up_udf("Name", "Seqno"))

df2 = df.withColumn("Name", up_udf(df["Name"], df["Seqno"]))

df2.printSchema()
df2.show()