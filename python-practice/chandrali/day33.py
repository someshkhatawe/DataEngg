# ********DAY 33********
# Python coding question:
#
# Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence.
# The function should return True if the sentence has any word with duplicate letters, else return False.


inp_sen_list="abf cd eff".split(" ")
c="False"
for word in inp_sen_list:
    word_list=list(word)
    word_set=set(word)
    if len(word_list)!=len(word_set):
        c="True"
        break
    else:
        continue
print(c)
