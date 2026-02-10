import re
def check(password):
    count=0
    feedback=[]
    
    if len(password)>=10:
        count+=1
    else:
        feedback.append('len of pass must be 10')
        
    if re.search(r"[a-z]",password):
        count+=1
    else:
        feedback.append('enter the lower case')
    
    if re.search(r"[A-Z]",password):
        count+=1
    else:
        feedback.append('ente the uppercase')
    
    if re.search(r"[0-9]",password):
        count+=1
    else:
        feedback.append('enter the number !')
    
    if re.search(r"[!@#$%^&*()]",password):
        count+=1
    else:
        feedback.append('pla enter the special case:')
    
    
    if count==5:
        print('this is strong pass')
    else:
        print('feedback for your pass is')  
    print(feedback)   
password="shant123"
check(password)