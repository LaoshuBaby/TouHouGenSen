a = [1, 2, 3, 4]
for i in a:
    for j in a:
        for k in a:
            if i != j and j != k and i != k:
                print(100 * i + 10 * j + k)
