class Rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        ar=self.l*self.b
        return ar
    def perimeter(self):
        p=2*(self.l+self.b)
        return p
x1=int(input("enter the area of first rectangle:"))
y1=int(input("enter the breadth of first rectangle:"))
r1=Rect(x1,y1)
print(f"area of rectangle",r1.area())
print(f"perimeter of rectangle",r1.perimeter())
x2=int(input("enter the area of second rectangle:"))
y2=int(input("enter the perimeter of second rectangle:"))
r2=Rect(x2,y2)
print(f"area of rectangle",r2.area())
print(f"perimeter of rectangle",r2.perimeter())
if r1.area()==r2.area():
    print("\n the area of both rectangle are equal")
else:
    print("\n the area of both rectangle are not equal")
    
