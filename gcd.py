a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
while b != 0:
    a, b = b, a % b
print("The gcd of the given numbers is:", a)

