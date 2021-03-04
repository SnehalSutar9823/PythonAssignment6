class Circle:
    PI=3.14
    def __init__(self,i,j,k):
        self.Radius=i
        self.Area=j
        self.Circumference=k

    def Accept(self):
        self.Radius=int(input("Enter Radius of Circle"))
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
        #print("Area of Circle is",self.Area)
    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius
        #print("Area of Circle is",self.Area)
    def Display(self):
        print("Radius of Circle is",self.Radius)
        print("Area of Circle is",self.Area)
        print("Circumference of Circle is",self.Circumference)
    
def main():
    
    Obj1=Circle(0.0,0.0,0.0)
    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()
    


if __name__=="__main__":
    main()
