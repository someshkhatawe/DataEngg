from pyspark import SparkContext
from pyspark.sql import SparkSession
import os

# Initialize a SparkContext and SparkSession
sc = SparkContext("local", "BroadcastExample")
# spark = SparkSession(sc)

sc.setLogLevel("DEBUG")

# Create the main dataset
data = [
    ("sam", "Computer Science", "US"),
    ("Mark", "Physics", "CA"),
    ("Jay", "Mathematics", "UK"),
    ("Kirk", "Musician", "FR"),
    ("Eric", "Finance", "DE"),
    ("Hano", "Videographer", "JP")
]

rdd = sc.parallelize(data)

# Define a lookup table (country code to country name)
lookup_data = {
    "US": "United States",
    "CA": "Canada",
    "UK": "United Kingdom",
    "FR": "France",
    "DE": "Germany",
    "JP": "Japan"
}

# Create a broadcast variable for the lookup table
broadcast_table = sc.broadcast(lookup_data)


# Define a function to map country codes to country names
def map_country_name(row_tuple):
    # print(type(row_tuple))
    country_code = row_tuple[2]
    country_name = broadcast_table.value.get(country_code, "Unknown")
    return (row_tuple[0], row_tuple[1], country_name)


# Use the broadcasted data within your transformation
result_rdd = rdd.map(map_country_name).collect()

# Show the results
# result_rdd.foreach(lambda x: print(x))

for i in result_rdd:
    print(i)

os.system("pause")

# Stop the SparkContext
# sc.stop()

