from bs4 import BeautifulSoup
from requests import get


def find_next_links(url):
    start_link = url
    page = get(start_link)
    bs = BeautifulSoup(page.content, 'html.parser')
    blog_pagination = bs.find('nav', class_='blog-pagination clear-fix numeric')
    page_links = blog_pagination.find_all('a')
    url_links = [link.get('href') for link in page_links]
    return url_links
