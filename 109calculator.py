# def format_name(f_name,l_name):
#     """Takes th elast functionsa
#     dlkfjakldf
#     adkjfald"""
#     return f"f_name.title() l_name.title()"

# print(format_name("jude kjahf","djflkd akdhf"))

# format_name()
from art import logo_calculator

print(logo_calculator)

def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n1 

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 /  n2



     
operators = {
"+":add,
"-":subtract,
"*":multiply,
"/":divide}

def calculator():
    num1 = float(input("What is the first number?: "))
    for operator in operators:
            print( operator)
    calculation_done = False
    while not calculation_done:
        
        operation_symbol = input("Pick an operation from the line above: ")
        if operation_symbol == "+":
            calcl_function = operators["+"]
        elif operation_symbol == "-":
            calcl_function = operators["-"]
        elif operation_symbol == "/":
            calcl_function = operators["/"]
        num2 = float(input("What is the next number?: "))
        answer = calcl_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        result = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start.: ").lower()
        if result == 'n':
            calculation_done = True 
            calculator()
        elif result == 'y':
            num1 = answer 

calculator()