def flatt(lst):
    flat = []
    
    for i in lst:
        if type(i) == list:
            flat += flatt(i)
        else:
            flat.append(i)
    
    return flat


print(flatt([[1, 2], [3, [4, 5]],[2,3,4,5]]))
