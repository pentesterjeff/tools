#!/bin/python

###########################################
# Crawler desenveloper for @Pentesterjeff #
# https://github.com/pentesterjeff        #
###########################################

import requests
import re
import time

site = raw_input('Enter a website: ')

to_crawl = ['http://' + site]

crawled = set()

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}
try:
    while True:
        url = to_crawl[0]
        try:
            req = requests.get(url, headers=header)
        except:
            to_crawl.remove(url)
            crawled.add(url)
            continue

        html = req.text
        links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
        print 'Crawling:', url

        to_crawl.remove(url)
        crawled.add(url)

        for link in links:
            if link not in crawled and link not in to_crawl:
                to_crawl.append(link)
except Exception as error:
    print 'Error...\nCalculating Errors'
    time.sleep(3)
    print error, str('### CHECK YOUR CONNECTION ###')
    print 'Usage: python crawler.py\nEnter a websiite: Domain.com (or) Domain.com.br'
