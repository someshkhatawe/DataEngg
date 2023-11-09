from pyspark.sql import SparkSession
import pyspark.sql.functions  as f

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()


# when and filter
# data = [("James","M",60000),("Michael","M",70000),
#         ("Robert",None,400000),("Maria","F",500000),
#         ("Jen","",None)]
#
# columns = ["name","gender","salary"]
# df = spark.createDataFrame(data = data, schema = columns)
#
#
# df2 =  df.select("*" , when(df.gender == 'M' , "male")
#                        .when(df.gender =='F', "Female")
#                         .when(df.gender.isNull(), " ")
#                         .otherwise(df.gender)
#                  .alias("new_gender"))
#
# df3 = df2.select("name", "salary").filter(" salary  >= 400000").show()

#  distinct count



data = [("James", "Sales", 3000),
    ("Michael", "Sales", 4600),
    ("Robert", "Sales", 4100),
    ("Maria", "Finance", 3000),
    ("James", "Sales", 3000),
    ("Scott", "Finance", 3300),
    ("Jen", "Finance", 3900),
    ("Jeff", "Marketing", 3000),
    ("Kumar", "Marketing", 2000),
    ("Saif", "Sales", 4100)
  ]
columns = ["employee_name","department","Salary"]
df = spark.createDataFrame(data=data,schema=columns)

# print(df.distinct().count())
#
# df2=df.select(f.countDistinct("department","Salary"))

# from pyspark.sql.window import Window
#
# windowSpec = Window.partitionBy("Department").orderBy(f.desc("salary"))
#
# df_sal = df.withColumn("rank", f.dense_rank().over(windowSpec)).filter("rank ==2")
# df_sal.show()

from functools import reduce  # For Python 3.x
from pyspark.sql import DataFrame


def unionAll(*dfs):
    return reduce(DataFrame.unionAll, dfs)


df1 = spark.createDataFrame([[1, 1], [2, 2]], ['a', 'b'])

# different column order.
df2 = spark.createDataFrame([[3, 333], [4, 444]], ['b', 'a'])
df3 = spark.createDataFrame([[555, 5], [666, 6]], ['b', 'a'])

# unioned_df = unionAll(df1, df2, df3)
# unioned_df.show()

# df1.union(df2).show()
import functools

def unionAll2(*dfs):
    return functools.reduce(lambda df1,df2: df1.union(df2), dfs)


m_df = unionAll2(df1,df2)

m_df.show()