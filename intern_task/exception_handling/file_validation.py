class MyFileNotFoundError(Exception):
    pass
try: 
    with open('s.csv','r') as file:
        date=file.read()
        print(date)
    
except FileNotFoundError :
    raise MyFileNotFoundError('file not found in system sorry!')
    
    