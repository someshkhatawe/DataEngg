# ********DAY 23********
# Python coding question:
#
# Write a program to find how many times substring “Emma” appears in the given string.
# input:
# str = "Emma is good developer. Emma is a writer"
# Output:
# Emma appeared 2 times

def count_v(s):
    count_d = 0
    for ch in s.split(" "):
        if ch.lower()=="emma":
            count_d+=1
    return count_d

print(count_v("Emma is good developer. Emma is a writer"))

