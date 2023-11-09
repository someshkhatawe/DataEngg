from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc ,udf, collect_list, initcap, base64, ascii, format_number, format_string,substring, concat, upper ,length
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName('PySpark_Tutorial').getOrCreate()


# deptData = [("Finance",10), ("Marketing",20),
#     ("Sales",30),("IT",40)
#   ]
# deptColumns = ["dept_name","dept_id"]
# deptDF=spark.createDataFrame(deptData,deptColumns)
# deptDF.show()

# def up(state):
#     return state.lower()

addData=[(1234567,"1523 Main St","SFO","abcdasea"),
    (2345345,"3453 Orange St","SFO","sdasd"),
    (3435346,"34 Warner St","Jersey","dsadaf"),
    (4435345,"221 Cavalier St","Newark","fdgdfg"),
    (5435346,"789 Walnut St","Sandiago","dfghbuy")
  ]
addColumns = ["emp_id","addline1","city","state"]
addDF = spark.createDataFrame(addData,addColumns)
# addDF.show()

# testudf = udf(up, StringType())

# df3 = addDF.withColumn("state", initcap((col("state"))))
# df3.show()


# df3 = addDF.withColumn("state", base64((col("state"))))
# df3.show()

# df3 = addDF.withColumn("emp_id2", format_number((col("emp_id")),0))
# df3.show()


# df3 = addDF.withColumn("len", length(col("state"))).withColumn("state2", concat(  upper( substring( (col("state") ),0,1))   , substring( col("state"),1, 20 ) ))
df3= addDF.selectExpr("*" , "concat(upper(substr(state , 0,1)) , substr(state , 1,length(state)-1    ) )   as name2")
df3.show()
# df3 = addDF.withColumn("state2", length(col("state")))
# df3.show()



# concat(upper(substr(state , 0,1)) , substr(state , 1,length(state)-1    ) )