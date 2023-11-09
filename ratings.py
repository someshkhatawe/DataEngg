
from pyspark import SparkContext, StorageLevel

sc = SparkContext("local[*]", "wordcount")

sc.setLogLevel("ERROR")

ratingsRdd = sc.textFile("F:/Trendy tech/Week 11/2.DAtasets/ratings.dat")

mappedRdd = ratingsRdd.map(lambda x: (x.split("::")[1],x.split("::")[2]))


newMapped = mappedRdd.mapValues(lambda x: (float(x), 1.0))


reducedRdd = newMapped.reduceByKey(lambda x,y : (x[0] + y[0], x[1] + y[1]))

filteredRdd = reducedRdd.filter(lambda x: x[1][0] > 10)


ratingsProcessed = filteredRdd.mapValues(lambda x : x[0] / x[1]).filter(lambda x : x[1] > 4.5)


moviesRdd = sc.textFile("F:/Trendy tech/Week 11/2.DAtasets/movies.dat")

mappedmoviesRdd = moviesRdd.map(lambda x: (x.split("::")[0],x.split("::")[1]))

joinedRdd = mappedmoviesRdd.join(ratingsProcessed)


result = joinedRdd.map(lambda x : x[1][0])

res = result.collect()

for i in res:
    print(i)

