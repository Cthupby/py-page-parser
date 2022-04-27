import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_links(url):
    ''' Get url of the page for parsing '''
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, "lxml")
    ''' List to collect urls which was found on page '''
    finded_url = []
    ''' To find urls in page '''
    links = soup.find_all("a", href=True)
    for link in links:
        if not link['href'].find('https://'):
            d_url = urlparse(link['href']).netloc
            finded_url.append('https://' + d_url)
    return list(set(finded_url))


if __name__ == '__main__':
    get_links()
