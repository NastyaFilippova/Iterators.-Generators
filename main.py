#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from pprint import pprint
import json

countries = []

class LinkIterator:
    def __init__(self, file, start=0):
        self.file = open(file, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1
        self.link = 'https://en.wikipedia.org/wiki/'

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.json):
            raise StopIteration
        country = self.json[self.start]['name']['common']
        country_link = self.link+country.replace(' ', '_')
        return f'{country}: {country_link} \n'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

if __name__ == '__main__':
    new_file = open('countries_link.txt', 'w', encoding='utf-8')

    with LinkIterator('countries.json') as linkitem:
        for country in linkitem:
            for country_link in country:
                new_file.write(country_link)
