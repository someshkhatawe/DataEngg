# ********DAY 13********
# Python coding question:
# Write a function that capitalizes the first and fourth letters of a name.
#
# TC 1:capitalize("chandrali")
#   'ChaNdrali'
# TC 2:capitalize("roy")
#    'Name is too short!'

def cap(a):
    res =""
    for i, ch in enumerate(a):
        if i == 0 or i == 3:
            res= res+ch.upper()

        else :
            res =res+ch
    return res



print(cap("hello"))

print(cap("chandrali"))
