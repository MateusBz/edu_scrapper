from bs4 import BeautifulSoup
from requests import get


def get_article_list(url_list):
    for url in url_list:
        page = get(url)
        bs = BeautifulSoup(page.content, 'html.parser')
        blog_name = bs.title.get_text()
        new_article_list = []
        for article in bs.find_all('li', class_='blog-grid-style'):
            article_header = article.find('header', class_='post-header')
            article_header_h2 = article_header.find('h2', class_='post-title')
            article_link = article_header_h2.find('a', href=True)['href']
            article_title = article_header_h2.find('a').get_text()
            article_date = article_header.find('span', class_='post-date').get_text()
            article_abstract = article.find('div', class_='post-content')
            article_abstract_text = article_abstract.find('p').get_text()
            try:
                article_img_url = article.find('img')['data-src']
            except Exception:
                article_img_url = None

            new_article = {
                'title': article_title,
                'article_url': article_link,
                'blog_name': blog_name,
                'abstract': article_abstract_text,
                'author': 'Monika',
                'image_url': article_img_url,
                'date': article_date
            }
            new_article_list.append(new_article)
    return new_article_list
