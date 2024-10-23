import random
import string

def generate_password(length):
    """Generate a random password of a specified length."""
    # Define the character sets to use for generating the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + punctuation

    # Generate a password using random choices from the combined character set
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    """Main function to run the password generator."""
    print("=== Welcome to the Password Generator ===")
    
    while True:
        # Prompt the user for the desired password length
        try:
            length = int(input("Please enter the desired length of your password (8-32 characters): "))
            if length < 8 or length > 32:
                print("Oops! Please enter a length between 8 and 32 characters.")
                continue
        except ValueError:
            print("Hmm, that's not a valid number! Please enter a number.")
            continue
        
        # Generate the password
        generated_password = generate_password(length)

        # Display the generated password
        print(f"\nHere is your generated password: {generated_password}\n")

        # Ask if the user wants to generate another password
        again = input("Would you like to generate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the password generator. Goodbye!")
            break

# Run the password generator
if __name__ == "__main__":
    main()
