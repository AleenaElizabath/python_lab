def gcd(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
print("The gcd of the given numbers is : ", end="")
print(gcd(a, b))
