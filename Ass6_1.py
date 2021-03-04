class Demo:
    Value=11
    def __init__(self,i,j):
        self.no1=i
        self.no2=j

    def Fun(self):
        print("Value of no1 and no2 from Fun is", self.no1,self.no2)

    def Gun(self):
        print("Value of no1 and no2 from Gun is", self.no1,self.no2)

def main():
    num1=int(input("Enter Number 1"))
    num2=int(input("Enter Number 2"))


    Obj1=Demo(num1,num2)
    Obj1.Fun()
    Obj1.Gun()
    num3=int(input("Enter Number 1"))
    num4=int(input("Enter Number 2"))


    Obj2=Demo(num3,num4)
    Obj2.Fun()
    Obj2.Gun()

    
    print("Value is",Obj1.Value)


if __name__=="__main__":
    main()
