import sys

def main():
    # Check that exactly one command-line argument is provided
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    # Ensure the file has a .py extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        # Open the file safely with UTF-8 encoding
        with open(filename, "r", encoding="utf-8") as f:
            count = 0
            for line in f:
                # Skip blank lines
                if line.strip() == "":
                    continue
                # Skip lines that are comments (after removing leading spaces)
                if line.lstrip().startswith("#"):
                    continue
                # Otherwise, count the line as code (includes docstrings)
                count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Print the total number of code lines
    print(count)

# Ensure main() runs only when the file is executed directly
if __name__ == "__main__":
    main()
