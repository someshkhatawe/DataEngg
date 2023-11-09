def rev_f(x):
    a = 0
    b = 1

    if x < 0:
        print("invalid")
    elif x == 0:
        return a
    elif x == 1:
        return b
    else:
        res = [None] * (x + 1)
        res[0], res[1] = a, b
        for i in range(2, x + 1):
            res[i] = res[i - 1] + res[i - 2]
    return res


print(rev_f(3))