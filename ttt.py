from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "Broadcast Country Codes Example")

# Define a read-only dataset of country codes and names
country_codes = {
    "US": "United States",
    "CA": "Canada",
    "UK": "United Kingdom",
    "FR": "France",
    "DE": "Germany",
    "JP": "Japan",
}

# Create a broadcast variable for the country codes
broadcast_country_codes = sc.broadcast(country_codes)

# Create an RDD with some data
data = ["US", "CA", "UK", "FR", "DE", "JP"]
rdd = sc.parallelize(data)

# Function to look up country names using the broadcasted country codes
def lookup_country_name(code):
    country_code_map = broadcast_country_codes.value
    return f"{code}: {country_code_map.get(code, 'Unknown')}"

# Use the broadcast variable to look up country names
result = rdd.map(lookup_country_name)

# Collect and print the results
print(result.collect())

# Stop the SparkContext
# sc.stop()