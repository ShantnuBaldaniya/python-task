def word_break(s,word):
    result=''
    for ch in s:
        result+=ch
        
        if result in word:
            result=''
        
    if result=='':
        return True
    else:
        return False
            
s='helloworld'
word=['world','hello']
print(word_break(s,word))

