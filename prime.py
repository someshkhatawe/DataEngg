def rev_f(x):
    if x > 1:
        res = []
        for num in range(2, x):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                res.append(num)
    else:
        pass
    return res


print(rev_f(100))