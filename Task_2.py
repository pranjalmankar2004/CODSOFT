import random
import string

def generate_password(length):
    # Define the character set for the password (you can customize this based on your requirements)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice()
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password you want to generate: "))
            if length <= 0:
                print("Password length should be greater than 0.")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation interrupted by the user.")
            break

if __name__ == "__main__":
    main()

