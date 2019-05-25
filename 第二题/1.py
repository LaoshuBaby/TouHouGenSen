a = [1, 2, 3, 1, 2, 3]
i = 0
while i != len(a):
    if a[i] in a[:i]:
        a.pop(i)
        i = i - 1
    else:
        i = i + 1
print(a)
