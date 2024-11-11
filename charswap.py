char=input("Enter a string")
char2=list(char)
char2[0],char2[-1]=char2[-1],char2[0]
char3="".join(char2)
print("The string after swapping first and last characters:",char3)
