csv_path = "E:\\code\\python-task\\intern_task\\json\\data.csv"
with open(csv_path,'r') as f:
    data=f.read()

lines = data.split("/n")
line_count = len(lines)

print(line_count)

words = data.split()
word_count = len(words)
print(word_count)

char_count=len(data)

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
        
    else:
        freq[word] = 1
print('freq',freq)

len_av=0
word=data.split()

for w in word :
    len_av+=len(w)

av=len_av/len(word)

print(av)

word = data.split()

longest = max(word, key=len)
shortest = min(word, key=len)

print("Longest word:", longest)
print("Shortest word:", shortest)

