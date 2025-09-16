from tabulate import tabulate
import sys
import csv
def main():
    try:
        if len(sys.argv) == 2:
            file = sys.argv[1]
            if file.endswith(".csv"):
                with open(file) as f:
                    reader = csv.DictReader(f)
                    data = list(reader)
                    #print(data)
                    print(tabulate(data,headers = "keys",tablefmt = "grid"))
            else:
                sys.exit("Not a CSV file")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line argumants")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
    except FileNotFoundError:
                sys.exit("File does not exist")

if __name__ == "__main__":
    main()
