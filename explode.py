import pyspark
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import  explode, explode_outer , posexplode , posexplode_outer

spark = SparkSession.builder.appName('pyspark-by-examples').getOrCreate()

arrayData = [
        ('James',['Java','Scala'],{'hair':'black','eye':'brown'}),
        ('Michael',['Spark','Java',None],{'hair':'brown','eye':None}),
        ('Robert',['CSharp',''],{'hair':'red','eye':''}),
        ('Washington',None,None),
        ('Jefferson',['1','2'],{})]

df = spark.createDataFrame(data=arrayData, schema = ['name','knownLanguages','properties'])
df.printSchema()


# df.select(df.name, explode(df.knownLanguages)).show()

df.describe



# df.select(df.name, explode_outer(df.knownLanguages)).show()
#
#
# df.select(df.name, posexplode_outer(df.knownLanguages)).show()

os.system("pause")