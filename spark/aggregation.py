
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName('PySpark_Tutorial').getOrCreate()

orders_data = (spark.read.format('csv')
               .option('inferSchema', "true")
               .load("F:/Trendy tech/12th week/1.Dataset/order_data.csv")
               .toDF('InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country')
               )
# orders_data.show()

# orders_data.groupby('country','InvoiceNo').agg(sum('Quantity').alias('tot'), sum(expr("Quantity *  UnitPrice ")).alias('IV')).show()


# orders_data.groupBy('country').count().show()
print(orders_data.select('country').count())