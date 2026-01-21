import sys
import os


def main():
    # Check number of arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # Check if file is a Python file
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if file exists
    if not os.path.exists(filename):
        sys.exit("File does not exist")

    # Count lines that are not blank and not comments
    count = 0
    with open(filename, "r") as file:
        for line in file:
            # Remove whitespace from start and end
            stripped = line.strip()

            # Ignore blank lines
            if stripped == "":
                continue

            # Ignore comments
            if stripped.startswith("#"):
                continue

            # Otherwise, it's a line of code
            count += 1

    print(count)


main()