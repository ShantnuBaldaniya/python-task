import re

email = "test@gmail.com or and cc@yahoo.com"

pattern = r"[a-zA-Z0-9._]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}"

match1 = re.match(pattern, email)
print(match1.group() if match1 else "Invalid Email")
print(match1.group())

word=match1.group().split('@')
print('Domain:',word[-1])
print('Username :',word[0])




