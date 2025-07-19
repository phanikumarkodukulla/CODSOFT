def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def get_user_numbers():
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    return first_num, second_num

def show_menu():
    print("\nWhat do you want to do?")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")

def main():
    print("Welcome to my calculator!")
    
    while True:
        show_menu()
        choice = input("Pick an option (1-4) or 'q' to quit: ")
        
        if choice == 'q':
            print("Thanks for using the calculator!")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Please pick a valid option")
            continue
            
        num1, num2 = get_user_numbers()
        
        if choice == '1':
            result = add_numbers(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract_numbers(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply_numbers(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide_numbers(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
                
        print()

if __name__ == "__main__":
    main()