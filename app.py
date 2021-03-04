import os

from find_next_links import find_next_links
from get_article_list import get_article_list

from dotenv import load_dotenv
load_dotenv()


def app():
    links = find_next_links(os.getenv('URL'))
    articles_list = get_article_list(links)
    return articles_list


if __name__ == '__main__':
    articles = app()
