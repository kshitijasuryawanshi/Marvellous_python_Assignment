class Employee:

    def __init__(self,A,B,C):     #constructor    
        self.name=A            #Instance Variable
        self.emp_id=B          #Instance Variable
        self.salary=C             #Instance Variable

    
    def DisplayInfo(self): 
        print("Employee Name:"+self.name)
        print("Employee city:",self.emp_id)
        print("Employee salary:",self.salary)
   

def main():
    emp1=Employee('Rahul',101,15000)    #object Creation
    emp2=Employee('Pooja',151,25000)    #object Creation

    print("Employee Name:"+emp1.name)
    print("Employee salary:",emp1.emp_id)
    print("Employee city:",emp1.salary)

    emp2.DisplayInfo()

    emp1.DisplayInfo()




if __name__=="__main__":
    main()