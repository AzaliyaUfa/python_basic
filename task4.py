dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}

d = {}
for i in dict:
    if dict[i] >= 3:
        d[dict[i]] = i
print(d)
