# coding: utf-8
import models
import requests
import json


def get_content(url):
    response = requests.get(url)
    return json.loads(response.content)


def parse(books, users):
    with open('title_author.txt', 'w') as f:
        for book in books:
            bm = models.BookModel(book['title'])
            bm.set_name_from_id(book['userId'], users)
            f.write('标题:{},  作者:{}\n'.format(bm.title, bm.name))


def main():
    url_book = 'https://jsonplaceholder.typicode.com/posts'
    url_users = 'https://jsonplaceholder.typicode.com/users'
    books = get_content(url_book)
    users = get_content(url_users)
    parse(books, users)


if __name__ == '__main__':
    main()
