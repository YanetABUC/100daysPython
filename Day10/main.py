from art import logo
#import replit



def add(number1, number2):
  return number1 + number2

def substract(number1, number2):
  return number1 - number2

def multiply(number1, number2):
  return number1 * number2

def divide(number1, number2):
  return number1 / number2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def process_operation(number1, number2, operation):
  function = operations[operation]
  result = function(number1, number2)

  print(f"{number1} {operation} {number2} = {result}")
  return result

end_program = False


while not end_program:
  print(logo)
  end_operation = False
  
  result = float(input("What's the first number?: "))
  for op in operations:
    print(op)
  
  while not end_operation:
    operation = input("Pick an operation: ")
    number = float(input("What's the next number?: "))
    result = process_operation(result, number, operation)
    next_step = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new operation:")
    
    if next_step == 'n':
      end_operation = True
      #replit.clear()
