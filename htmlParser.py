import urllib.request
from html.parser import HTMLParser

links = set()

def get_html_from_url(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode("utf8")


class CacParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and attr[1].endswith(".csv"):
                    links.add(attr[1])

page_root = "https://support.spatialkey.com/spatialkey-sample-csv-data/"
html = get_html_from_url(page_root)
parser = CacParser()
parser.feed(html)

for i, link in enumerate(links):
    html = get_html_from_url(link)
    f = open("./html/" + str(i) + ".csv", "w")
    f.write(html)
    f.close()
