num=int(input("Enter the range:"))
f1=0
f2=1
print(f1)
print(f2)
for i in range(0,num):
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
