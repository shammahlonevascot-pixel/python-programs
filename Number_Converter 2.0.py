#Shammahlon T.Evasco
#26-4144-869

import time

MENU_CHOICES = {
    "1": 10,  # Decimal
    "2": 2,   # Binary
    "3": 8,   # Octal
    "4": 16,  # Hexadecimal
}

BASE_NAMES = {2: "Binary", 8: "Octal", 10: "Decimal", 16: "Hexadecimal"}

MAX_FAILED_ATTEMPTS = 3
PENALTY_SECONDS = 10

DIGITS_FOR_BASE = {
    2: "01",
    8: "01234567",
    10: "0123456789",
    16: "0123456789ABCDEF",
}


def is_valid_number(number_str, base):
    #Return True only if every character is a valid digit for the given base.
    if number_str == "":
        return False
    allowed = DIGITS_FOR_BASE[base]
    return all(ch in allowed for ch in number_str.upper())


def convert_number(number_str, base):
    """Convert number_str (interpreted in the given base) to all four bases."""
    value = int(number_str, base)
    return {
        2: bin(value)[2:],
        8: oct(value)[2:],
        10: str(value),
        16: hex(value)[2:].upper(),
    }


def apply_penalty():
    #Lock the program for PENALTY_SECONDS after too many failed attempts.
    print(f"\nToo many invalid attempts! Locked for {PENALTY_SECONDS} seconds...")
    for remaining in range(PENALTY_SECONDS, 0, -1):
        print(f"  Please wait... {remaining}s remaining", end="\r")
        time.sleep(1)
    print(" " * 40, end="\r")  # clear the countdown line
    print("Penalty over. You may try again.\n")


def print_menu():
    print("Select Original Base:")
    print("1. Decimal (Base 10)")
    print("2. Binary (Base 2)")
    print("3. Octal (Base 8)")
    print("4. Hexadecimal (Base 16)")
    print("5. STOP (exit program)")


def main():
    print("=== Number System Converter ===\n")

    failed_attempts = 0

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "5" or choice.upper() == "STOP":
            print("\nProgram terminated. Goodbye!")
            break

        if choice not in MENU_CHOICES:
            failed_attempts += 1
            print("ERROR! Please enter a valid choice (1-5).\n")
            if failed_attempts >= MAX_FAILED_ATTEMPTS:
                apply_penalty()
                failed_attempts = 0
            continue

        base = MENU_CHOICES[choice]

        number_input = input(f"Enter a {BASE_NAMES[base]} number: ").strip()

        if not is_valid_number(number_input, base):
            failed_attempts += 1
            print("ERROR!\n")
            if failed_attempts >= MAX_FAILED_ATTEMPTS:
                apply_penalty()
                failed_attempts = 0
            continue

        # Successful conversion resets the failed-attempt counter
        failed_attempts = 0

        results = convert_number(number_input, base)
        print("Converted Outputs:")
        print(f"Base 2: {results[2]}")
        print(f"Base 8: {results[8]}")
        print(f"Base 10: {results[10]}")
        print(f"Base 16: {results[16]}")
        print()


if __name__ == "__main__":
    main()
