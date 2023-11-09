from pyspark.sql import SparkSession
from pyspark.sql.functions import count, desc, col, max, struct

spark = SparkSession.builder.appName('PySpark_Tutorial').getOrCreate()

df_genre = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(
    "C:/Users/Som-Pc/Downloads/genre.csv")

column_list = df_genre.columns
column_list = list(map(lambda x:x.upper(), column_list))
print(column_list)


# df_genre.printSchema()


# df_listenings = spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(
#     "C:/Users/Som-Pc/Downloads/listenings.csv")
#
# df_rihana = df_listenings.select("user_id").filter(" artist  == 'Rihanna' ").groupBy("user_id").agg(
#     count("user_id").alias("count")).orderBy(col("count").desc())

# df_rihana.show(truncate=False)

# df3 = df_listenings.select("artist", "track").groupBy("artist", "track").agg(count("*").alias("Count")).orderBy(desc("Count")).limit(10)


# df4 = df_listenings.filter(" artist == 'Rihanna' ").groupBy("user_id").count("user_id").alias("count").orderBy(col("count").desc())
#
#
# df4.show()