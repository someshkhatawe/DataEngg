from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

spark = SparkSession.builder.appName('ProjectPro').getOrCreate()

data = [("James", "Sales", 3000), \
 ("Michael", "Sales", 4600), \
 ("Robert", "Sales", 4100), \
 ("Maria", "Finance", 3000), \
 ("James", "Sales", 3000), \
 ("Scott", "Finance", 3300), \
 ("Jen", "Finance", 3900), \
 ("Jeff", "Marketing", 3000), \
 ("Kumar", "Marketing", 2000), \
 ("Saif", "Sales", 4100) \
 ]
column= ["employee_name", "department", "salary"]
df = spark.createDataFrame(data = data, schema = column)
# df.show()
# df2 = df.dropDuplicates()
df.write.format("csv").mode("overwrite").save("F:\workingdir\drop_duplicates" ,headers= True)

# df3 = df.distinct()

df.write.format("csv").mode("overwrite").save("F:\workingdir\distinct", headers= True)
