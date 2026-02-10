import re
text='9099748482  +91 1234567890 and +911234567890'
pattern=r"\+?\d{0,3}?\s?\d{10}"

match=re.findall(pattern, text)
#print(match)
count=0
for num in match:
    count+=1
    clean=num.replace(" ","")
    print(count," ",clean)

    if clean.startswith("+91") and len(clean)==13:
        print('valid indian number')
    else:
        print("this is not indian number")