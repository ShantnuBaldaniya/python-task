f = open("data.csv", "r")

for line in f:
    print(line.replace(",", "\t"), end="")

f.close()
