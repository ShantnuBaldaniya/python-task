
def check_arm(number):
   

    n = len(number)         
    sum1 = 0


    for digit in number:
        sum1 += int(digit) ** n


    if sum1 == int(number):
        print("Yes,  Armstrong number")
    else:
        print("No, not an Armstrong number")

number = input("Enter a number to check if it's Armstrong or not: ")
check_arm(number)
