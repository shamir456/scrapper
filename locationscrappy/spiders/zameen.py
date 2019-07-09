# -*- coding: utf-8 -*-
import scrapy
import json


class ZameenItem(scrapy.Item):
	name=scrapy.Field()
	slug=scrapy.Field()
	
		
class ZameenSpider(scrapy.Spider):
    name = 'zameen'
    allowed_domains = ['zameen.com']
    start_urls = ['https://www.zameen.com/api/internalLinks/searchPage/?purpose=for-rent&location=%2FLahore-1&category=Homes','https://www.zameen.com/api/internalLinks/searchPage/?purpose=for-rent&location=%2FIslamabad-3&category=Homes',
    'https://www.zameen.com/api/internalLinks/searchPage/?purpose=for-rent&location=%2FKarachi-2&category=Homes','https://www.zameen.com/api/internalLinks/searchPage/?purpose=for-rent&location=%2FRawalpindi-41&category=Homes']
    login_url='https://www.zameen.com/'
    i=0

    def parse(self, response):
    	citi=['Lahore','Islamabad','Karachi','Rawalpindi']

    	print("procesing:"+response.url)
    	jsonresponse = json.loads(response.body.decode("utf-8"))

        
        for records in jsonresponse["locations"]:
        	print(records)
        	
         	scraped_info={
         		"name":records['location']['name'],
         		"url":'https://www.zameen.com/api/internalLinks/searchPage/?purpose=for-rent&location=%2F'+records["location"]["slug"].replace('/','')+'&category=Homes',
         		"city":citi[self.i],
         		"id":self.i+1

         		}
         	yield scraped_info

    	self.i=self.i+1

    def parse_locations(self,response):

    	check=response.css('a._2dd261fc::text').extract()
        location=zip(response.url,check)

        for item in location:
        	scraped_info={
        	'page':response.url,
        	#'location':item[0],
        	'check':item[1]
        	}


        	yield scraped_info

    	
