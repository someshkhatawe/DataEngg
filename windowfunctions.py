from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, row_number,percent_rank , ntile, when,dense_rank
from pyspark.sql.window import Window

spark = spark = SparkSession.builder.appName('PySpark_Tutorial').getOrCreate()

df1 = spark.read \
    .format("csv") \
    .option("sep", ",") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("F:\sparkpractice\data\products.txt")

df1.show()

# df1.printSchema()
# df1.select("price").show()
# windowspecs = Window.partitionBy("product_category").orderBy(desc("price"))
#
# # df2 = df1.withColumn("row_num", percent_rank().over(windowspecs))
# df2 = df1.withColumn("bucket", ntile(3).over(windowspecs))
# df3 = df2.withColumn("phone_range", when(df2.bucket == 1,"Expesive")\
#     .when(df2.bucket == 2,"Mid Range").otherwise("cheap"))
# df3.show(truncate=False)


windpspec = (Window.partitionBy("brand")
             .orderBy(desc('price')))


df2 = df1.withColumn('rank', dense_rank().over(windpspec)).filter( "rank <=2 ")

df2.printSchema()

df2.show()
