
    
num1=int(input("Enter number 1 :  "))
num2=int(input("Enter number 2 :  "))    
def add(num1,num2):
    print(num1+num2) 
def sub(num1,num2):
    print(num1-num2) 
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2) 
    
def calculator(cal,num1,num2):
    cal(num1,num2)
    
calculator(add,num1,num2)


calculator(sub,num1,num2)


calculator(mul,num1,num2)


calculator(div,num1,num2)
    

    
    
    

    