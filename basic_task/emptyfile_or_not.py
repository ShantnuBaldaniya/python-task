file=open('file.txt','r')
data=file.read()

if data=='':
    print('file is empty ')
else:
    print('file not empty ')

file.close()
    