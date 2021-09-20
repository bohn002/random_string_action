import os
import string
import random

def main():
    letters = ""
    char_type = os.environ['INPUT_CHAR_TYPE']
    char_length = int(os.environ['INPUT_CHAR_LENGTH'])
    if char_type == "lower":
        letters = string.ascii_lowercase
    elif char_type == "upper":
        letters = string.ascii_uppercase
    else:
        letters = string.ascii_letters
    r_string = ''.join(random.choice(letters) for i in range(char_length))
    set_output(r_string)

def set_output(cmd):
    print(f"::set-output name=random_string::{cmd}", flush=True)

if __name__ == "__main__":
    main()