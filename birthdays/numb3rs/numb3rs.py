import re
import sys
def main():
    address = input("Enter IPv4 address")
    print(validate(address))
def validate(address):
    address = address.split(".")
    try:
        if len(address) != 4:
            return False
        for i in address:
            if not i.isdigit() or not 0 <= int(i) <= 255:
                return False
        return True
    except ValueError:
        return False
if __name__ == "__main__":
    main()
