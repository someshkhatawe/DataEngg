# ********DAY 10********
# Python coding question:
#
# Write a Python function to multiply all the numbers in a list.
#
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def ml_l(x):
    res = 1
    for i in x:
        res = res * i
    return res


print(ml_l([1, 2, 3, -4]))
