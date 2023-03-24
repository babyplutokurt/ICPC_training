def remove(s):
    count = 1
    pointer = s[0]
    for c in range(len(s)):
        if s[c] != pointer:
            count += 1
            pointer = s[c]
    return count


a = '101011011001010'
print(remove(a))
