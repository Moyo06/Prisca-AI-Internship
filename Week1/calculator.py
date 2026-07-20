print("---------Welcome to Moyo's calcultor--------")
while True:
   print("1. Addition(+)")
   print("2. Subtraction(-)")
   print("3. Multiplication(*)")
   print("4. Division(/)")
   
   choice = input(" choose a number between 1 to 4")

   if choice not in ["1", "2", "3", "4"]:
      print("Invalid choice, choose betwwen number 1 to 4")
      continue

   while True:
      try:
        number1 = float(input("Enter the first number"))
        number2 = float(input("Enter the second number"))
        break
      except ValueError:
         print("Please enter valid numbers, try again.")
         
   if choice == "1":
      print("Result:", number1 + number2)
   elif choice == "2":
      print("Result:", number1 - number2)
   elif choice == "3":
      print("Result:", number1 * number2)
   elif choice == "4":
      if number2 == 0: 
         print("Undefined")
      else:
         print("Result:", number1 / number2)
   
   again = input("Do you want to continue?(yes/no): ")
   
   if again.lower() != "yes":
      print("Thanks for using my calculator")
      break
