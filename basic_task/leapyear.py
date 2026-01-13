year=int(input('enter the year to check leap or not:'))
if year%4==0 and year%100!=0:
    print('yes, it is leap year')
else:
    print('no,it is not leap year')
    