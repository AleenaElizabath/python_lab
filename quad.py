from math import*
a=float(input("Enter 1st coefficient"))
b=float(input("Enter 2nd coefficient"))
c=float(input("Enter 3rd coefficient"))
eqn=b**2-(4*a*c)
if eqn>=0:
    r1=(-b+sqrt(eqn))/(2*a)
    r2=(-b-sqrt(eqn))/(2*a)
    print("Roots=",r1," and ",r2)
else:
    r=-b/(2*a)
    i=sqrt(-eqn)/(2*a)
    print("roots are",r,"+",i,"i and ",r,"-",i,"i")
