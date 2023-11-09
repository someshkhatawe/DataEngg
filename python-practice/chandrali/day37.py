# 2. Write a prggram to sort the elements in odd
# positions in descending order and elements in
# ascending order


def ascsort(l):
    odd = sorted(l[0:: 2], reverse=True)
    print(odd)
    even = sorted(l[1:: 2])
    print(even)
    res = [None] * len(l)
    res[0::2] = odd
    res[1:: 2] = even
    return res


print(ascsort([13, 2, 4, 15, 12, 10, 5]))
