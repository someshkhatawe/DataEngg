def remove_consec_duplicates(s):
    new_str = ""
    prev = ""

    for ch in s:
        if len(new_str) ==0:
            new_str+=ch
            prev =ch
        if ch==prev:
            continue
        else:
            new_str+=ch
            prev =ch

    return new_str

print(remove_consec_duplicates("aaabbcccdeffghkkklaaa"))