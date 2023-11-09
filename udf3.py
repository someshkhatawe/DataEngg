from pyspark.sql import SparkSession
import pyspark.sql.functions  as f
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()


columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

df = spark.createDataFrame(data=data,schema=columns)

def up(x,y):
    return x.upper() +str(y)

up_udf = f.udf(lambda x,y : up(x,y),StringType())

df2= df.withColumn("Name", up_udf("Name" ,"Seqno"))

df2.show()

columns2= ["a" ,"b"]
data2 = [("1","abc"),
        ("2","xyz"),
        ("3","mnop")]
df3 = spark.createDataFrame(data=data2 , schema=columns2)

df4= df3.withColumn("c", up_udf("a" ,"b"))

df4.show()