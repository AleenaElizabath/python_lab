string=input("Enter a string:")
for i in string:
    freq= string.count(i)
    print(str(i) + ": " + str(freq), end=", ")
