# -*- coding: utf-8 -*-
import scrapy
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import re
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class SeleniumScrapperSpider(scrapy.Spider):
    name = 'selenium_scrapper'
    allowed_domains = ['zameen.com']
    start_urls = ['https://www.zameen.com/add_property_single.html']

    # def __init__(self):
    #     self.driver = webdriver.Firefox()
    def __init__(self):
    	options = FirefoxOptions()
    	options.add_argument("--disable-notifications")
    	options.add_argument("--headless")
    	binary = FirefoxBinary('/usr/bin/firefox')
        self.driver = webdriver.Firefox(options=options,firefox_binary=binary)





    def parse(self, response):
    	arr=['Lahore']
    	time.sleep(5)

    	all_iframes = self.driver.find_elements_by_tag_name("iframe")
    	if len(all_iframes) > 0:
		    print("Ad Found\n")
		    self.driver.execute_script("""
		        var elems = document.getElementsByTagName("iframe"); 
		        for(var i = 0, max = elems.length; i < max; i++)
		             {
		                 elems[i].hidden=true;
		             }
		                          """)
		    print('Total Ads: ' + str(len(all_iframes)))


        
        for a in arr:
        	self.driver.get(response.url)
        	self.driver.refresh()
        	time.sleep(10)
        	self.driver.execute_script("return document.getElementById('city').setAttribute('style', 'display:inline-block;');")
        	select = Select(self.driver.find_element_by_name('city'))

	        select.select_by_visible_text(a)
	        time.sleep(4)
	        sel = scrapy.Selector(text=self.driver.page_source)
	        location=sel.xpath('//*[@id="_cat_selector_3"]/option/text()').extract()
	        print(location)
	        location=zip(location)
	        city={
	        a:[]

	        }
	        i=1
	        

	        for x in location[510:]:
	        	array=[]
	        	# Area={
	        	#  'location':x[0],
	        	#  'id':i,
	        	#  'sub_location': None
	        	# }
	        	time.sleep(2)
	        	#yield Area
	        	

	        	select = Select(self.driver.find_element_by_name('_cat_selector_3'))
	        	select.select_by_visible_text(x[0])
	        	print('Setting Location')
	        	time.sleep(3)
	        	sel = scrapy.Selector(text=self.driver.page_source)
	        	geo_Location=sel.xpath('//*[@id="map_field"]/@value').extract()
	        	print('Location geo_Location',geo_Location)
	        	time.sleep(2)
	        	
	        	Area={
	        	 'location':x[0],
	        	 'id':i,
	        	 'sub_location': None,
	        	 'geo_Location':geo_Location
	        	}
	        	i=i+1
	        	print(Area)
	        	#yield Area
	        	print(i)



	        	

	        	if sel.xpath('//*[@id="_cat_selector_4"]/option/text()') :


	        		sub_location=sel.xpath('//*[@id="_cat_selector_4"]/option/text()').extract()
	        		print(sub_location)
	        		self.driver.refresh()
	        		self.driver.get(response.url)
	        		time.sleep(6)
	        		self.driver.execute_script("return document.getElementById('city').setAttribute('style', 'display:inline-block;');")
	        		select = Select(self.driver.find_element_by_name('city'))
	        		select.select_by_visible_text(a)
	        		time.sleep(4)
	        		select = Select(self.driver.find_element_by_name('_cat_selector_3'))
	        		select.select_by_visible_text(x[0])
	        		time.sleep(3)


	        		j=1

	        		for sub in sub_location:
	        			#time.sleep(3)
	        			print(sub.strip())
	        			time.sleep(1)

	        			select = Select(self.driver.find_element_by_name('_cat_selector_4'))
	        			select.select_by_visible_text(sub.strip())
	        			time.sleep(5)
	        			page_source = scrapy.Selector(text=self.driver.page_source)

	        			
	        			geo_subLocation=page_source.xpath('//*[@id="map_field"]/@value').extract()
	        			print('Geo Sub Location Field',geo_subLocation)
	        			print('Setting SubLocation')
	        			scraped_info={
				    	
				    	'name':sub,
				    	'locationId':Area["id"],
				    	'geo_subLocation':geo_subLocation

				    	}
				    	array.append(scraped_info)

				    	print(j)

				    	# if j%3==0:
			      #   		self.driver.refresh()
			      #   		self.driver.get(response.url)
				     #    	time.sleep(6)
				     #    	self.driver.execute_script("return document.getElementById('city').setAttribute('style', 'display:inline-block;');")
				     #    	select = Select(self.driver.find_element_by_name('city'))

					    #     select.select_by_visible_text(a)
					    #     time.sleep(4)
					    #     select = Select(self.driver.find_element_by_name('_cat_selector_3'))
	        # 				select.select_by_visible_text(x[0])
	        # 				time.sleep(3)
	        	
					    #     sel = scrapy.Selector(text=self.driver.page_source)

				    	j=j+1
				    	print('After append')

				    	#yield scraped_info
	        		Area['sub_location']=array


	        	# if i%15==0 :
	        	# 	self.driver.refresh()
	        	# 	self.driver.get(response.url)
		        # 	time.sleep(3)
		        # 	self.driver.execute_script("return document.getElementById('city').setAttribute('style', 'display:inline-block;');")
		        # 	select = Select(self.driver.find_element_by_name('city'))

			       #  select.select_by_visible_text(a)
			       #  time.sleep(4)
			       #  sel = scrapy.Selector(text=self.driver.page_source)
	        		#yield Area

	        	yield Area
	        	city[a].append(Area)
	        	
	        self.driver.refresh()
	        		      		
	        yield city



        # time.sleep(5)
        # for x in location:
        #     select = Select(self.driver.find_element_by_name('_cat_selector_3'))
        #     select.select_by_visible_text(x)
        #     time.sleep(5)
        #     sel = scrapy.Selector(text=self.driver.page_source)
        #     location=sel.xpath('//*[@id="_cat_selector_3"]/option/text()').extract()

        #     #sel = scrapy.Selector(text=self.driver.page_source)
            
        #     if sel.xpath('//*[@id="_cat_selector_4"]/option/text()') :
        #     	sub_location=sel.xpath('//*[@id="_cat_selector_4"]/option/text()').extract()
        #     	for i in sub_location:
			    	# scraped_info={
			    	
			    	# 'name':i,
			    	# 'locationId':x["id"]

			    	# }
			    	# yield scraped_info




        


