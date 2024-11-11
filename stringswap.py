str1=input("Enter the first string:")
str2=input("Enter the second string:")
str3=str1+str2
str4=list(str3)
str4[0],str4[-1]=str4[-1],str4[0]
str5="".join(str4)
print(str5)
