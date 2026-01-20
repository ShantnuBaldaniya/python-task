arr = [
    [5, 9, 1],
    [3, 7, 8],
    [4, 6, 2]
]
max=0
sl=0
for i in arr:
    for j in i:
        if j>max:
            sl=max
            max=j
        elif j>sl and j!=max:
            sl=j
print(sl)