def merge():
    a=open('file.txt','r')
    b=open('f1.txt','r')
    c=open('output_file.txt','w')

    while True:
        line1=a.readline()
        line2=b.readline()
        
        if line1=='' and line2=='':
            break
        if line1!='':
            c.write(line1)
        if line2!='':
            c.write(line2)
            
    a.close()
    b.close()
    c.close()
    
merge()