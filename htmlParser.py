import urllib.request
from html.parser import HTMLParser

links = []

def get_html_from_url(url, codec = "utf8"):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode(codec)


class CacParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and attr[1].endswith("/file"):
                    links.append(attr[1])

page_root = "http://www.correlatesofwar.org/data-sets/state-system-membership"
html = get_html_from_url(page_root)
parser = CacParser()
parser.feed(html)


for i in range(len(links)):
    # first two are PDFs
    if (i in [0,1]):
        continue
    urllib.request.urlretrieve(links[i], "./html/" + str(i) + ".csv")
