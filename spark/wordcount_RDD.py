from pyspark import SparkContext, StorageLevel

sc = SparkContext("local[*]", "premiumusers")

rdd1 = sc.textFile("F:/Trendy tech/wordcount.txt")

rdd2= rdd1.flatMap(lambda x:x.split(" "))

rdd3 = rdd2.map(lambda x: (x.upper(),1))

rdd4 = rdd3.reduceByKey(lambda x,y: x+y)


print(rdd3.groupByKey(lambda x,y: x+y))

# rdd4.saveAsTextFile("F:/Trendy tech//spark/output/")

# print(rdd4.collect())

# for (word, count) in rdd4.collect():
#     print("%s: %i" % (word, count))


# rdd5 = rdd4.reduceByKey(lambda x,y:x+y)
#
# print(rdd5.collect())
#
# rdd6 = rdd5.map(lambda x:(x[0], x[1]))
# print('rdd6','\n')
#
# print(rdd6.collect())

# ---

# words = sc.textFile("F:/Trendy tech/wordcount.txt").flatMap(lambda line: line.split(" "))
#
# wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
#
#
# wordCounts.saveAsTextFile("F:/Trendy tech//spark/output/")



#

# text_file = sc.textFile("F:/Trendy tech/wordcount.txt")
# counts = text_file.flatMap(lambda line: line.split(" ")) \
#                             .map(lambda word: (word, 1)) \
#                            .reduceByKey(lambda x, y: x + y)
#
# output = counts.collect()
# for (word, count) in output:
#     print("%s: %i" % (word, count))




