# ********DAY 21********
# Python coding question:
#
# Write a Python code to accept a string and count the number of vowels and consonants.
# Print them separately.

def count_v(s):
    count_d ={"v":0 , "c":0}
    for ch in s:
        if ch.lower() in ('a','e','i','o','u'):
            count_d["v"]+=1
        elif ch != " ":
            count_d["c"] += 1
    return count_d

print(count_v("PratHik KiNi M"))