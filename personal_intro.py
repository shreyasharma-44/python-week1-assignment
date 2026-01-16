"""
Personal Introduction Program
This program asks for user information and displays a welcome message.
Author: [Your Name]
Date: [Today's Date]
"""

def main():
    # Display program title
    print("=" * 50)
    print("       PERSONAL BIO-DATA PROGRAM       ")
    print("=" * 50)
    
    # Get user information
    name = input("What is your name? ")
    age = input("How old are you? ")
    hobby = input("What is your favorite hobby? ")
    city = input("Which city do you live in? ")
    favorite_food = input("What's your favorite food? ")
    
    # Display the welcome message
    print("\n" + "=" * 50)
    print("          YOUR PROFILE          ")
    print("=" * 50)
    
    print(f"👋 Name: {name}")
    print(f"🎂 Age: {age}")
    print(f"❤️  Hobby: {hobby}")
    print(f"🏙️  City: {city}")
    print(f"🍕 Favorite Food: {favorite_food}")
    
    print("\n" + "=" * 50)
    print(f"Welcome to the program, {name}!")
    print(f"Great to know you love {hobby}!")
    print("Thanks for sharing your information! 😊")
    print("=" * 50)

# Run the program
if __name__ == "__main__":
    main()