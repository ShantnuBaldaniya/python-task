class handler:
    def show(self,value):
       
        if type(value)==int:
            return 'this is a integer value'
        elif type(value)==float:
            return 'this is a float'
        elif type(value)==str:
            return 'this is a string'
        elif type(value)==bool:
            return 'this is a boolian'
h=handler()
print(h.show(12))
print(h.show('strte'))
print(h.show(123.3232))

        
        
    
    