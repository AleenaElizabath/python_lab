yr=int(input("Enter the year"))
if (yr%4==0 and yr%100!=0) or yr%400==0:
    print("leap year")
else:
    print("Not a leap year")
