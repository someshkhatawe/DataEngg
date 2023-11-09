# ********DAY 20********
# Python coding question:
#
# Write a function in Python that accepts a credit card number.
# It should return a string where all the characters are hidden with an asterisk except the last four.
# For example, if the function gets sent "4444444444444444", then it should return "4444".

def masking_credit_card_number(card_number):
    if len(card_number) < 14:
        raise ValueError("Please enter valid cardnumber")

    return "*" * (len(card_number) - 4) + card_number[-4:]


