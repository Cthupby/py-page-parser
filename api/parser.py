import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# url = "https://losst.ru"


def get_links(url):
    '''
    Url of document for a parsing
    '''
    r = requests.get(url=url)
    '''
    Making soup
    '''
    soup = BeautifulSoup(r.text, "lxml")
    ''' To store events data '''
    finded_url = []
    '''
    To find all links in page
    '''
    links = soup.find_all("a", href=True)
    for link in links:
        if not link['href'].find('https://'):
            d_url = urlparse(link['href']).netloc
            finded_url.append('https://' + d_url)
    return list(set(finded_url))


if __name__ == '__main__':
    get_links()
