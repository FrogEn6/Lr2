#!/usr/bin/env python3
import sys
import re

def validate_name(name):
    return re.fullmatch(r'[a-z][a-zA-Z]*', name) is not None

def from_file():
    try:
        with open('names.txt', 'r') as file:
            names = file.read().splitlines()
    except FileNotFoundError:
        print("The file names.txt not found.")
        return

    errors = []
    for name in names:
        if validate_name(name):
            print(f"Hello, {name}!")
        else:
            errors.append(f"Wrong name: {name}")

    if errors:
        with open('error.txt', 'w') as error_file:
            for error in errors:
                error_file.write(error + '\n')

def interactive():
    print("Enter the names one at a time. To exit, press Ctrl+C.")
    try:
        while True:
            name = input("Enter a name: ").strip()
            if validate_name(name):
                print(f"Hello, {name}!")
            else:
                print(f"Error: The name '{name}' contains invalid characters or does not start with a lowercase letter.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'interactive':
        interactive()
    else:
        from_file()

if __name__ == "__main__":
    main()
