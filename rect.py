class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    
    def area(self):
        area=self.__length*self.__breadth
        print("Area=",area)
        return area

    def perimeter(self):
        per=2*(self.__length+self.__breadth)
        print("Perimeter=",per)
        return per

    def __lt__(self,other):
        return self.area() < other.area()
l1=int(input("Enter the length of the first rectangle"))
b1=int(input("Enter the breadth of the first rectangle"))
l2=int(input("Enter the length of the second rectangle"))
b2=int(input("Enter the breadth of the second rectangle"))
obj=Rectangle(l1,b1)
obj2=Rectangle(l2,b2)
obj.area()
obj.perimeter()
obj2.area()
obj2.perimeter()
if obj<obj2:
    print("Rectangle1 is greater")
else:
    print("Rectangle2 is greater")

