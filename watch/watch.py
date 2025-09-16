import re
import sys
def main():
    parse(input("HTML: "))

def parse(s):
    if matches := re.search(r'iframe(.*)? src=\"(?P<s_url>https?://(www\.)?youtube\.com/embed/)(?P<after_embed>[^"]+)',s):
        short_url = matches.group('s_url')+ matches.group('after_embed')
        final_url = re.sub(matches.group('s_url'),"https://youtu.be/",short_url)
        return final_url
    else:
        return
if __name__ == "__main__":
    main()
