class Arithematic:
    
    def __init__(self,i,j,k):
        self.Value1=i
        self.Value2=j
        self.Ans=k

    def Accept(self):
        self.Value1=int(input("Enter Number 1"))
        self.Value2=int(input("Enter Number 2"))
        
    def Addition(self):
        self.Ans=self.Value1+self.Value2
        return self.Ans
    def Substarction(self):
        self.Ans=self.Value1-self.Value2
        return self.Ans
    def Multiplication(self):
        self.Ans=self.Value1*self.Value2
        return self.Ans
    def Division(self):
        self.Ans=self.Value1//self.Value2
        return self.Ans
    
    
def main():
    
    Obj1=Arithematic(0,0,0)
    ans=Obj1.Accept()
    ans=Obj1.Addition()
    print("Addition is",ans)
    
    ans=Obj1.Substarction()
    print("Substarction is",ans)
    
    ans=Obj1.Multiplication()
    print("Multiplication is",ans)
    
    ans=Obj1.Division()
    print("Division is",ans)
    


if __name__=="__main__":
    main()
