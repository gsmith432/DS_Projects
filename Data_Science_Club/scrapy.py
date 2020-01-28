#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:15:46 2017

@author: gabrielsmith
"""

import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']
    
fetch("https://www.reddit.com/r/gameofthrones/")
view(response)
response.css("...").extract()
reponse.css("...").extract_first()