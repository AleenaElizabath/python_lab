class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        area=self.length*self.breadth
        print("Area=",area)

    def perimeter(self):
        per=2*(self.length+self.breadth)
        print("Perimeter=",per)
    
obj=Rectangle(length,breadth)
l1=int(input("Enter the length of the first rectangle"))
b1=int(input("Enter the breadth of the first rectangle"))
l2=int(input("Enter the length of the second rectangle"))
b2=int(input("Enter the breadth of the second rectangle"))
a1,p1=obj.area(l1,b1),obj.perimeter(l1,b1)
a2,p2=obj.area(l2,b2),obj.perimeter(l2,b2)
print(a1)
print(p1)
print(a2)
print(p2)


