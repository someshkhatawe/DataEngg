x= 'Hannah'

def pal(x):
    for ch in range(0,len(x)//2):
        if x[ch].lower() != x[len(x)-ch-1].lower():
            return print("not palindrome")

    return print('palindrome')

pal(x)