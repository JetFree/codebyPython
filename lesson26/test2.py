import base64
import binascii
import sys
import urllib.parse
import codecs


def print_actions():
    print("1 - encode\n2 - decode")


def print_formats():
    print("Select the desired format: BASE64, BASE32, BASE16, URLENCODE, HEX, ROT13")


def get_action():
    try:
        print_actions()
        return int(input("Selected action: "))
    except KeyboardInterrupt:
        print("Program interrupted by user")
        sys.exit(0)


def do_encoding(string):
    base64_r = base64.b64encode(bytes(string, 'utf-8')).decode('utf-8')
    base32_r = base64.b32encode(bytes(string, 'utf-8')).decode('utf-8')
    base16_r = base64.b16encode(bytes(string, 'utf-8')).decode('utf-8')
    urlencode_r = urllib.parse.quote(string)
    hex_r = '\\' + '\\'.join(hex(ord(c))[1:] for c in string)
    print(f"BASE64 {'==>': >8}   {base64_r}")
    print(f"BASE32 {'==>': >8}   {base32_r}")
    print(f"BASE16 {'==>': >8}   {base16_r}")
    print(f"URLENCODE {'==>': >5}   {urlencode_r}")
    print(f"HEX {'==>': >11}   {hex_r}")
    print(f"ROT13 {'==>': >9}   {codecs.encode(string, ' rot_13')}")


def do_decoding(format, string):
    try:
        if format == "BASE64":
            print(f"BASE64  ==>  {base64.b64decode(bytes(string, 'utf-8')).decode('utf-8')}")
        elif format == "BASE32":
            print(f"BASE32  ==>  {base64.b32decode(bytes(string, 'utf-8')).decode('utf-8')}")
        elif format == "BASE16":
            print(f"BASE16  ==>  {base64.b16decode(bytes(string, 'utf-8')).decode('utf-8')}")
        elif format == "URLENCODE":
            print(f"URLENCODE  ==>  {urllib.parse.unquote(string)}")
        elif format == "HEX":
            backslash_char = "\\"
            print(
                f"HEX  ==>  {codecs.decode(string.replace(backslash_char, '').replace('x', ''), 'hex').decode('utf-8')}")
        elif format == "ROT13":
            print(f"ROT13  ==>  {codecs.decode(string, 'rot_13')}")
        else:
            print("Wrong coding selected, correct options are: BASE64, BASE32, BASE16, URLENCODE, HEX, ROT13")
    except binascii.Error:
        print("Look like incorrect value entered for this coding")


def do_action(action):
    try:
        if action == 1:
            string = input("Enter text: ")
            do_encoding(string)
        elif action == 2:
            print_formats()
            format = input("Enter format: ")
            string = input("Enter text: ")
            do_decoding(format, string)
        else:
            print("Wrong option selected. Correct options are: 1 or 2")
    except InterruptedError:
        print("Program interrupted by user")
        sys.exit(0)


if __name__ == "__main__":
    action = get_action()
    do_action(action)
