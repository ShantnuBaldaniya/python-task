ip = input("Enter IP: ")

dot = 0

for i in ip:
    if i == '.':
        dot = dot + 1

if dot == 3:
    print("Valid IP")
else:
    print("Invalid IP")
