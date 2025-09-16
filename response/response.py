from validator_collection import checkers
def main():
    print(validate_email(input("Email: ")))
def validate_email(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"
if __name__ == "__main__":
    main()






