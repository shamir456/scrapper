# -*- coding: utf-8 -*-
import scrapy


class LocationSpider(scrapy.Spider):
    name = 'location'
    allowed_domains = ['zameen.com']
    start_urls = ['https://www.zameen.com/all_locations/Karachi-2-1-1.html']

    def parse(self, response):
        area=response.css('a').extract()
        url=response.xpath('/html//div[contains(@id, "sub-location-list")]//a/@href()').extract()
        text=response.xpath('/html//div[contains(@id, "city-button")]').extract()
        location=zip(response.url,area,url,text)

        for item in location:
        	scraped_info={
        	'page':item[0],
        	'area':item[1],
        	'url':item[2],
        	'text':item[3]
        	}


        	yield scraped_info

    