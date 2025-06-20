class Rectangle:

    def __init__(self,A,B):     #constructor    
        self.width=A            #Instance Variable
        self.length=B          #Instance Variable
                               

    def ComputeAreaAndPerimeter(self): 
        Area=0
        Area=self.width*self.length
        perimeter=0
        perimeter=2*(self.length+self.width)
        print("Area:",Area,"Perimeter:",perimeter)
        

   

def main():
    emp1=Rectangle(5,10)    #object Creation

    emp1.ComputeAreaAndPerimeter()

if __name__=="__main__":
    main()