#Simple Calculator
def calculate():
  """
  This function performs basic arithmetic operations based on user input.
  """
  # Get user input for numbers
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
  except ValueError:
    print("Invalid input. Please enter numbers only.")
    return

  # Get user input for operation
  operation = input("Choose an operation (+, -, *, /): ")

  # Perform calculation based on operation
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 - num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    if num2 == 0:
      print("Error: Division by zero.")
      return
    result = num1 / num2
  else:
    print("Invalid operation. Please choose +, -, *, or /.")
    return

  # Display the result
  print(f"The result is: {result}")

# Run the calculator
while True:
  calculate()
  # Ask user if they want to continue
  user_choice = input("Do you want to perform another calculation? (y/n): ")
  if user_choice.lower() != 'y':
    break

print("Thank you for using the calculator!")
