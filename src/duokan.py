#!/usr/bin/env python
# encoding=utf-8

from workflow import web


def book_items():

    web_data = web.get('http://book.duokan.com/store/v0/web/rank/fresh?start=0&page_length=20').json()

    for book_item in web_data['items']:
        book_data = {
            'title': book_item['title'],
            'subtitle': book_item['summary'],
            'arg': u"http://www.duokan.com/book/{}".format(book_item['sid']),
            'uid': u'{}'.format(book_item['sid']),
            'valid': True,
        }
        yield book_data
