
from urllib import request
from bs4 import BeautifulSoup
from lxml import etree


URL = 'https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table'

def get_page(url):
    response = request.urlopen(url)
    return response


def get_xpath(page, xpath):
    htmlparser = etree.HTMLParser()
    tree = etree.parse(page, htmlparser)
    return tree.xpath(xpath)


def parse_table(table):
    res = {}
    for row in table.find_all('tr')[1:]:
        country = row.find_all('th')[0].text
        medals = {}
        medals['rank'], medals['gold'], medals['silver'], medals['bronze'], medals['total'] = \
            [int(x.text) for x in row.find_all('td')]
        print(medals)
        res[country] = medals

    return res


def main():
    page = get_page(URL)
    soup = BeautifulSoup(page, 'html.parser')
    return parse_table(soup.select('table.wikitable.sortable.plainrowheaders')[0])


if __name__ == '__main__':
    main()
