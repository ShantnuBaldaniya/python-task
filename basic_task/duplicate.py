a = [1, 2, 3, 2, 4, 1, 5]

duplicate = []
list = []

for i in a:
    if i in list and i not in duplicate:
        duplicate.append(i)
    else:
        list.append(i)
        
print("Dupli:", duplicate)
print(list)
