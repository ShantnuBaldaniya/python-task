d1 = {'a': 6, 'b': 8, 'c': 9}
d2 = {'b': 8, 'c': 9, 'd': 3}

res = {}

for k in d1:
    res[k] = d1[k]
for k in d2:
    if k in d1:
        res[k] = d1[k] + d2[k]
    else:
        res[k] = d2[k]
        
print(res)





