key = "1.1000.0".split()
ver = "2.0.0".split()
for i in range(len(key)):
    if key[i] < ver[i]:
        raise ValueError
print(key)