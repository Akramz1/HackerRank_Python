# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")


html = ""
n = int(input())
for _ in range(n):
    html += input()

parser = MyHTMLParser()
parser.feed(html)
