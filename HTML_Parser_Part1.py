# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
n = int(input())


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrbs):
        print("Start :", tag)
        for attr in attrbs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrbs):
        print("Empty :", tag)
        for attr in attrbs:
            print(f"-> {attr[0]} > {attr[1]}")


html = ""
for _ in range(n):
    html += input()

parser = MyHTMLParser()
parser.feed(html)
