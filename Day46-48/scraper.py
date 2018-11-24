# from requests_html import HTMLSession
import requests
import bs4


# URL of site we want to scrape
URL = "https://www.pythonforbeginners.com/"

# session = HTMLSession()

def pull_site():
    # raw_site_page = session.get(URL) #Pull down the site.
    # raw_site_page.raise_for_status()  #Confirm site was pulled. Error if not
    # raw_site_page = raw_site_page.html.render()
    raw_site_page = requests.get(URL)
    return raw_site_page

def scrape(site):
    header_list = []
    #Create BeautifulSoup object
    soup = bs4.BeautifulSoup(site.text, 'lxml')

    h2s = soup.find_all("h2")
    for h2 in h2s:
        header_list.append(h2.find('a').attrs['href'])

    print(header_list)
    # h2s = site.html.find('h2')
    # print(h2s)
    # for h2 in h2s:
    #     print(h2.a)

        # print(h2.a.string)
    # for links in site.html.find('href'):
    #     print(links)
    # html_list = site.html.links
    # print(html_list.html.absolute_links)
    # print(site.html.absolute_links)

    # all_li = soup.find_all('bookmark')
    #
    # for title in all_li:
    #     print(title.string)

    # for link in soup.find_all('h2'):
    #     print(link)
        # link_list = link.get('href')
        # print(link_list)

    # for link in soup.findAll('h2'):
    #     print(link)
    #     # print(bs4.SoupStrainer('a href'))
    #     # print(link.get('href'))
    #
    # for link in soup.findAll('h2', attrs={'href': re.compile("^https://")}):
    #     print(link.get('href'))


    # all_class = soup.p['class']
    #
    # for title in all_class:
    #     print(title)
    #     print(title.string)
    # html_header_list = soup.select('.projectHeader')
    #
    # for headers in html_header_list:
    #     header_list.append(headers.getText())
    # for headers in header_list:
    #     print(headers)


if __name__ == "__main__":
    site = pull_site()
    scrape(site)