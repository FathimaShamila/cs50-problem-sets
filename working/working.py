import re
import sys
def main():
    print(convert(input("Hours: ")))

def convert(s):
    matches = re.search(r"(?P<h1>1[0-2]|[1-9])(?::(?P<m1>[0-5][0-9]))?\s(?P<p1>AM|PM)\sto\s(?P<h2>1[0-2]|[0-9])(?::(?P<m2>[0-5][0-9]))?\s(?P<p2>PM|AM)",s)
    if matches:
       h1 = int(matches.group('h1'))
       h2 = int(matches.group('h2'))
       m1 = int(matches.group('m1') or 0)
       m2 = int(matches.group('m2') or 0)
       p1 = matches.group('p1')
       p2 = matches.group('p2')
       time1 = convert_to_24(h1,m1,p1)
       time2 = convert_to_24(h2,m2,p2)
       result = f"{time1} to {time2}"
       return result
    else:
        raise ValueError("Invalid format")


def convert_to_24(hours,minutes,period):
    if period == "AM":
        if hours == 12:
            hours = 0
    else:
        if hours!= 12:
            hours +=12
    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
