# ********DAY 11********
# Python coding question:
#
# Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(s):
    res =""
    for ch in s:
        res= res + ch*3

    return res

print(paper_doll("Mississippi"))

