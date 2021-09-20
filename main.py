import os
import string
import random

def main():
    char_type = os.environ['INPUT_CHAR_TYPE']
    char_length = os.environ['INPUT_CHAR_LENGTH']
    match char_type:
        case "lower":
            letters = string.ascii_lowercase
        case "upper":
            letters = string.ascii_uppercase
        case _:
            letters = string.ascii_letters
    r_string = ''.join(random.choice(letters) for i in range(char_length))
    set_output(r_string)

def set_output(cmd):
    print(f"::set-output name=random_string::{cmd}", flush=True)

if __name__ == "__main__":
    main()