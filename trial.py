import sys

def get_char():
    try:
        # For Python 2
        return chr(ord(sys.stdin.read(1)))
    except TypeError:
        # For Python 3
        import msvcrt
        return msvcrt.getch().decode()

def print_ansi_escape_sequence(char):
    # Convert the character to its ANSI escape sequence
    ansi_escape = f"\u001b[{ord(char)}m"  # This is a basic example using the ASCII value of the character
    print(f"The ANSI escape sequence for '{char}' is: {ansi_escape}")

def main():
    print("Press any key to get the ANSI escape sequence. Press 'q' to quit.")
    while True:
        key = get_char()
        if key == 'q':
            print("Exiting the program.")
            break
        print_ansi_escape_sequence(key)

if __name__ == "__main__":
    main()
