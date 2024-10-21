a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))
op=" "
print('''Calculator:
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exponent
6.Exit''')
while(op!=6):
    op=int(input("Enter the operation(1/2/3/4/5/6):"))
    if op==1:
        print("Sum=",a+b)
    elif op==2:
        print("Difference=",a-b)
    elif op==3:
        print("Product=",a*b)
    elif op==4:
        print("Quotient=",a/b)
    elif op==5:
        print(a," to the power of ",b,"=",a**b)
    elif op==6:
        print("Exit!!")
        break
    else:
        print("Invalid input!")
        


