def chain(pair):
    pair.sort(key=lambda x:x[1])
    print(pair)
    c =0
    end =0
    for a,b in pair:
        print(end,a,b)
        if a < b:
            if end < a:
                c = c+1
                end =b
                print(c)
    return c
p=[(10, 7), (3, 4), (4,5),(2,3)]
print(chain(p))
