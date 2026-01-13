def check_argm(s1,s2):
    if len(s1)!=len(s2):
        return False

    for ch in s1:
        c1 = 0
        c2 = 0

        for i in s1:
            if i == ch:
                c1 += 1

        for j in s2:
            if j == ch:
                c2 += 1
        
    return True

string1=input('enter the 1st string:')
string2=input('enter the 2nd string:')

if check_argm(string1,string2):
    print("Anagram")
else:
    print("Not Anagram")

