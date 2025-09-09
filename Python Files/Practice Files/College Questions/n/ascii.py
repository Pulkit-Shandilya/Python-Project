# Program to print the ASCII value of a character and vice versa

# Input from the user
choice = input("Choose an option:\n1. Character to ASCII\n2. ASCII to Character\nEnter 1 or 2: ")

if choice == '1':
    # Character to ASCII
    character = input("Enter a character: ")
    if len(character) == 1:
        print(f"The ASCII value of '{character}' is {ord(character)}")
    else:
        print("Please enter a single character.")
elif choice == '2':
    # ASCII to Character
    try:
        ascii_value = int(input("Enter an ASCII value: "))
        if 0 <= ascii_value <= 127:
            print(f"The character for ASCII value {ascii_value} is '{chr(ascii_value)}'")
        else:
            print("Please enter a valid ASCII value (0-127).")
    except ValueError:
        print("Please enter a valid integer.")
else:
    print("Invalid choice. Please enter 1 or 2.")