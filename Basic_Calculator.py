while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Please choose operation: ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print("The Addition of two number is:",result)
        elif choice == '2':
            result = num1 - num2
            print("The Subtraction of two number is:",result)
        elif choice == '3':
            result = num1 * num2
            print("The Multiplication of two number is:",result)
        elif choice == '4':
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 /num2
            print("The Divisible of two number is:",result)
        else:
          print("Invalid input")

    again = input("Do you want to perform another calculation? (YES/NO): ")
    if again.upper() != 'YES':
        print("GOODBYE !SEE YOU SOON!!!")
        break
