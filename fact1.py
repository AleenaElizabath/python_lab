num=int(input("Enter a number:"))
fact=1
if num<0:
    print("Invalid")
else:
    for i in range(1,num+1):
        fact*=i
print("Factorial=",fact)
