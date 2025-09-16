import sys

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) == 2:
        if not sys.argv[1].endswith('.py'):
            sys.exit("Not a Python file")
        else:
            try:
                with open(sys.argv[1]) as f:
                    lines = f.readlines()
                    filtered_lines =[line for line in lines if not line.lstrip().startswith("#") and line.strip()]
                    print(len(filtered_lines))
            except FileNotFoundError:
                    sys.exit("File does not exist.")

if __name__ == "__main__":
    main()
