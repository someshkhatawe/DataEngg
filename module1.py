from pyspark import SparkContext, StorageLevel

sc = SparkContext("local[*]", "premiumusers")

base_rdd = sc.textFile("F:/Trendy tech/week 9/datasets/customer-orders.csv")

mapped_input = base_rdd.map(lambda x: (x.split(',')[0], float(x.split(',')[2])))

total_by_customer = mapped_input.reduceByKey(lambda x, y: x + y)

premium_customers = total_by_customer.filter(lambda x: x[1] > 5000)

doubled_amount = premium_customers.map(lambda x: (x[0], [1] * 2))


result = doubled_amount.collect()

for x in result:
    print(result)


print(doubled_amount.count())