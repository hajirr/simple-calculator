from art import logo
from replit import clear

print(logo)

def calc():
  result = 0
  first_number = float(input("first number : "))
  isContinue = True
  while isContinue:
    operator = input('''
    +
    -
    *
    /
    Choose the operator
    ''')
    second_number = float(input("next number : "))
    if operator == "+":
      result = first_number + second_number
    elif operator == "-":
      result = first_number - second_number
    elif operator == "*":
      result = first_number * second_number
    elif operator == "/":
      result = first_number / second_number
    
    print(f'''
        ===============
        RESULT {result}
        ===============
      ''')
    isNext = input("type 'y' for next calculation ").lower()
    if isNext == 'y':
      first_number = result
    else:
      print(f'''
        ===============
        RESULT: {result}
        ===============
      ''')
      isContinue = False
      calc() #Recursion
calc()
clear()