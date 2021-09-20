import os

def main():
    char_type = os.environ['INPUT_CHAR_TYPE']
    char_length = os.environ['INPUT_CHAR_LENGTH']
    set_output("boop")

def set_output(cmd):
    print(f"::set-output name=random_string::{cmd}", flush=True)

if __name__ == "__main__":
    main()