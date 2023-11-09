# importing the datetime package
import datetime

# given epoch time
epoch_time = 1648631418834

# using the datetime.fromtimestamp() function
date_time = datetime.datetime.fromtimestamp(epoch_time)

# printing the value
print("Given epoch time:", epoch_time)
print("Converted Datetime:", date_time)