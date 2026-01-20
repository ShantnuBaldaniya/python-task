def chunk_list(lst, size):
    result = []
    for i in range(0, len(lst), size):   
        result.append(lst[i:i+size])
    return result
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
chunk_size = 3

output = chunk_list(my_list, chunk_size)
print(output)
