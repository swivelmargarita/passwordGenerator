import random
import string
import argparse
import pyperclip


class PasswordGenerator:
    def __init__(self):
        self.letters_lower: str = string.ascii_lowercase
        self.letters_upper: str = string.ascii_uppercase
        self.digits: str = string.digits
        self.symbols: str = string.punctuation
        self.possible_chars: str = self.letters_lower + self.letters_upper + self.digits + self.symbols
        self.password_len: int = 10
        self.min_num_of_symbols: int = 2
        self.min_num_of_digits: int = 2
        self.min_num_of_upper_letters: int = 1
        self.password = []

    def change_len_of_password(self, new_len: int):
        self.password_len = new_len

    def change_min_num_of_symbols(self, new_min_num_of_symbols: int):
        self.min_num_of_symbols = new_min_num_of_symbols

    def change_min_num_of_digits(self, new_min_num_of_digits: int):
        self.min_num_of_digits = new_min_num_of_digits

    def change_min_num_of_upper(self, new_min_num_of_upper: int):
        self.min_num_of_upper_letters = new_min_num_of_upper

    def parse_arguments(self) -> None:
        parser = argparse.ArgumentParser()

        parser.add_argument("--length", metavar="n")
        parser.add_argument("--min-digits", metavar="n")
        parser.add_argument("--min-symbols", metavar="n")
        parser.add_argument("--min-upper", metavar="n")

        args: argparse.Namespace = parser.parse_args()
        try:
            if args.length:
                self.change_len_of_password(int(args.length))
            if args.min_digits:
                self.change_min_num_of_digits(int(args.min_digits))
            if args.min_symbols:
                self.change_min_num_of_symbols(int(args.min_symbols))
            if args.min_upper:
                self.change_min_num_of_upper(int(args.min_upper))
        except ValueError as e:
            raise SystemExit(f"ERROR! Must be type integer.\n{e}")

    def generate_password(self) -> str:
        [self.password.append(random.choice(self.digits)) for _ in range(self.min_num_of_digits)]
        [self.password.append(random.choice(self.symbols)) for _ in range(self.min_num_of_symbols)]
        [self.password.append(random.choice(self.letters_upper)) for _ in range(self.min_num_of_upper_letters)]
        chars_left_to_fill = self.password_len - (
                self.min_num_of_digits + self.min_num_of_symbols + self.min_num_of_upper_letters)
        [self.password.append(random.choice(self.possible_chars)) for _ in range(chars_left_to_fill)]
        random.shuffle(self.password)
        self.password = "".join(self.password)
        return self.password

    def copy_to_clipboard(self):
        try:
            pyperclip.copy(text=self.password)
        except Exception as e:
            print(f"Couldn't copy to the clipboard.\n{e}")


def main():
    pass_generator = PasswordGenerator()
    pass_generator.parse_arguments()
    password = pass_generator.generate_password()
    print(password)
    pass_generator.copy_to_clipboard()


if __name__ == "__main__":
    main()
