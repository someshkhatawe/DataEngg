# ********DAY 12********
# Python coding question:
#
# Write a code to check whether a year is leap year or not.
# Note:A year that is evenly divisible by 100 is a leap year only if it is also evenly divisible by 400.
#
# Desired Output:
# is_leap(1996)-->Leap year
# is_leap(2100)-->not a Leap year
# is_leap(2000)—>Leap year


def leap_year(year):
    """
    function to check whether a year is a leap year or not.

    Argument: 'year' is an integer input
    """
    if year % 100 == 0 and year % 400 == 0:
        return print('Leap year')

    elif year % 4 == 0 and not (year % 100 == 0):
        return print('Leap year')

    elif year % 4 == 0 and year % 100 == 0:
        if year % 400 == 0:
            return print('Leap year')

    return print('Not a leap year')


leap_year(1996)  # ==> Not a leap year
leap_year(2100)  # ==> Not a leap year
leap_year(2000)  # ==> Leap year