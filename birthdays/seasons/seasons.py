from datetime import datetime
from datetime import date
import inflect
import sys
def main():
    user_date = input("Date of Birth: ")
    try:
        birth_date = parse_date(user_date)
        result = date_in_words(birth_date)
        print(result)
    except ValueError:
        sys.exit("Invalid date")
        #result = date_in_words(birth_date)
        #print(f"{result.capitalize()} minutes")

def parse_date(s):
    return datetime.strptime(s,"%Y-%m-%d").date()

def date_in_words(d):
    date_diff = date.today() - d
    date_diff_mts = int(date_diff.total_seconds()/60)
    p = inflect.engine()
    result_date = p.number_to_words(date_diff_mts,andword="")
    return f"{result_date.capitalize()} minutes"
if __name__ == "__main__":
    main()

