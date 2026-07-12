print("---------Welcome to Moyo's calcultor--------")
while True:
   print("1. Addition(+)")
   print("2. Subtraction(-)")
   print("3. Multiplication(*)")
   print("4. Division(/)")
   
   choice = input(" choose between number 1 to 4")

   if choice not in ["1", "2", "3", "4"]:
      print("Invalid choice, choose betwwen number 1 to 4")
      continue

   number1 = int(input("Enter the first number"))
   number2 = int(input("Enter the second number"))

      
   if choice == "1":
      print(number1 + number2)
   elif choice == "2":
      print(number1 - number2)
   elif choice == "3":
      print(number1 * number2)
   elif choice == "4":
      if number2 == 0: 
       print("Undefined")
       continue
      print(number1 / number2)
   
   again = input("Do you want to continue?(yes/no): ")
   
   if again != "yes":
      print("Thanks for using my calculator")
      break
