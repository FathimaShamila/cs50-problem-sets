import sys
import csv
def main():
    try:
        if len(sys.argv) == 3:
            from_file = sys.argv[1]
            to_file = sys.argv[2]
            with open(from_file) as f,open(to_file,"w") as g:
                reader = csv.DictReader(f)
                writer = csv.DictWriter(g,fieldnames = ["first","last"] + reader.fieldnames[1:])
                writer.writeheader()
                for row in reader:
                    last,first = row["name"].split(",")
                    row["first"] = first.strip()
                    row["last"] = last.strip()
                    del row["name"]
                    writer.writerow(row)

        elif len(sys.argv) < 3:
            sys.exit("Too few comman-line arguments")
        else:
            sys.exit("Too many command-line aruguments")
    except (PermissionError,FileNotFoundError):
        sys.exit(f"Could not read {sys.argv[1]}")
if __name__ == "__main__":
    main()
