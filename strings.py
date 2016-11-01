# josh dickey 10/28/16
# this program encodes and decodes messages


def run_program():
    """this allows the user to encode, decode, or quit"""
    x = input("press e to encode, d to decode, or q to quit")
    if x == "e":
        encode()
    if x == "d":
        decode()
    if x == "q":
        print("have a good day")


def encode():
    """this encodes a message"""
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = int(input("select a number to encode your message"))
    inverted = alphabet[shift:] + alphabet[:shift]
    message = input("please enter a message to encode")
    for y in message:
        result += inverted[alphabet.index(y)]
    print(result)


def decode():
    """this decodes a message"""
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = int(input("select a number to decode your message"))
    inverted = alphabet[shift:] + alphabet[:shift]
    message = input("please enter a message to decode")
    for y in message:
        result += alphabet[inverted.index(y)]
    print(result)


def main():
    """this is the main function that runs the program"""
    run_program()


main()
