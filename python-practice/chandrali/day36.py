# ********DAY 36********
# Python coding question:
#
# You are given two numbers a and b. Create a function that returns the next number greater than a and b and divisible by b.
# Examples
# divisible_by_b(17, 8) ➞ 24
#
# divisible_by_b(98, 3) ➞ 99
#
# divisible_by_b(14, 11) ➞ 22


def divisible_by_b(a,b):
    num=a+1
    while (num%b!=0):
        num+=1
    print(num)

divisible_by_b(17, 8)