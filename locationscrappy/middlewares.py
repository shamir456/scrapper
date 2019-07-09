# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1200x600')

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False

# driver = webdriver.Firefox(capabilities=cap, executable_path=r'/usr/bin/geckodriver')
# binary = FirefoxBinary('/usr/bin/firefox')
# driver=webdriver.Firefox(firefox_binary=binary)
#driver = webdriver.Firefox(executable_path=r'/usr/lib/firefox')

class LocationscrappySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LocationscrappyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        arr=[{"id":56,"value":"3560","name":"Defence View Society","emirateId":1},
                {"id":57,"value":"1469","name":"Dehra Narathar","emirateId":1},
                {"id":58,"value":"3561","name":"Delhi Colony","emirateId":1},
                {"id":59,"value":"6675","name":"DHA City Karachi","emirateId":1},
                {"id":60,"value":"3563","name":"Dhabeji","emirateId":1}]
        driver.get(request.url)
        time.sleep(10)
        driver.execute_script("return document.getElementById('city').setAttribute('style', 'display:inline-block;');")
        select = Select(driver.find_element_by_name('city'))
        select.select_by_visible_text('Karachi')



        time.sleep(10)
        for x in arr:
            select = Select(driver.find_element_by_name('_cat_selector_3'))
            select.select_by_visible_text(x["name"])
            body = driver.page_source
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
