f=open('file.txt','r')
text=f.read()
f.close()


old_word=input('enter the word to find:')
new_word=input('enter the word replce:')

text=text.replace(old_word,new_word)
f=open('file.txt','w')
f.write(text)
f.close()
 
file=open(('file.txt'),'r')
text=file.read()
print(text)