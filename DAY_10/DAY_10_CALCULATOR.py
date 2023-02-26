#DAY-10
import art  
def add(n1,n2):
    return n1+n2
    
def subtract(n1,n2):
    return n1-n2
   
def multiply(n1,n2):
    return n1*n2
    
def divide(n1,n2):
    return n1/n2

def exponential(n1,n2):
    return n1**n2  

operations = {
"+":add,
"-":subtract,
"*":multiply,
"/":divide, 
'^':exponential
}
def calculator():
    print(art.logo)
    num1=float(input("Enter the first number: ")) 
    for symbols in operations:
        print(symbols)
    continues=True
    while continues:     
        operation_todo=input('Enter the operation: ')
        num2=float(input("Enter the second nummber: "))
        calculation=operations[operation_todo]
        answer=calculation(n1=num1,n2=num2)        
        print(f"{num1} {operation_todo} {num2} = {answer}")    
        if input(f"Type Y to continue calculation  with {answer} or Type N to exit: ")=='y':
            num1 = answer
        else:
            continues=False     
            
calculator()



