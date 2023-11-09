from pyspark import SparkContext, StorageLevel

sc = SparkContext("local[*]", "premiumusers")



rdd = sc.parallelize([(1, 'apple'), (2, 'banana'), (1, 'orange'), (2, 'grape')])
grouped_rdd = rdd.groupByKey()
# print(grouped_rdd.collect())

for (word, count) in grouped_rdd.collect():
    print((word, count))
    for r in count:
        print(r)