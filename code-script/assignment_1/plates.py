def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        length_is_valid(s)
        and starts_with_letters(s)
        and has_only_letters_numbers(s)
        and numbers_at_end(s)
        and first_number_not_zero(s)
    )


def length_is_valid(s):
    return 2 <= len(s) <= 6


def starts_with_letters(s):
    return s[:2].isalpha()


def has_only_letters_numbers(s):
    return s.isalnum()


def numbers_at_end(s):
    for i, ch in enumerate(s):
        if ch.isdigit():
            return s[i:].isnumeric()
    return True


def first_number_not_zero(s):
    for ch in s:
        if ch.isdigit():
            return ch != "0"
    return True


main()