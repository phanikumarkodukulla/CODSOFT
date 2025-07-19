import random
import string

def get_all_chars():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return letters + numbers + symbols

def make_password(length):
    all_chars = get_all_chars()
    password = ""
    
    for i in range(length):
        password += random.choice(all_chars)
    
    return password

def ask_user_for_length():
    while True:
        try:
            length = int(input("How long should your password be? "))
            if length <= 0:
                print("Please enter a number greater than 0")
                continue
            return length
        except ValueError:
            print("Please enter a valid number")

def ask_for_complexity():
    print("\nChoose password type:")
    print("1. Simple (letters and numbers only)")
    print("2. Complex (letters, numbers, and symbols)")
    
    while True:
        choice = input("Pick 1 or 2: ")
        if choice in ['1', '2']:
            return choice
        print("Please choose 1 or 2")

def make_simple_password(length):
    chars = string.ascii_letters + string.digits
    password = ""
    
    for i in range(length):
        password += random.choice(chars)
    
    return password

def run_generator():
    print("Password Generator")
    print("-" * 20)
    
    while True:
        length = ask_user_for_length()
        complexity = ask_for_complexity()
        
        if complexity == '1':
            new_password = make_simple_password(length)
        else:
            new_password = make_password(length)
        
        print(f"\nYour new password is: {new_password}")
        
        another = input("\nWant another password? (y/n): ")
        if another.lower() != 'y':
            print("Thanks for using the password generator!")
            break

if __name__ == "__main__":
    run_generator()