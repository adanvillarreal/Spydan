import scrapy
import csv
import sys
from scrapy.spiders.init import InitSpider
from scrapy.utils.response import open_in_browser
from scrapy.http.cookies import CookieJar
from spydan.items import SpydanItem
import subprocess
import argparse


#spydan -s mysql,
class LoginSpider(InitSpider):
    name = 'Spydan'
    #you can modify the following lists alongside with the query to filter your search in Shodan.io
    login_page = 'https://account.shodan.io/login'

    inquery = 'https://www.shodan.io/search?query='
    #Include the networks you want to scan in the list called nets
    start_urls = []
    #You can modify the search query here. It is shown here with port, but you could also search for products or services. Shodan.io only shows 5 pages of results (circa 50 results), so use the queries wisely.


    def __init__(self, category='', domain=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.nets = eval(nets)
        self.services = eval(services)
        self.products = eval(products)
        self.ports = eval(ports)
        self.username = username
        self.password = password
        for net in self.nets:
            for port in self.ports:
                for x in range(1,6):
                    start_urls.append(('https://www.shodan.io/search?query=net:%s'
                        '+port:%s&page=%s') % (net, port, str(x)))
            for service in self.services:
                for x in range(1,6):
                    start_urls.append(('https://www.shodan.io/search?query=net:%s'
                        '+service:%s&page=%s') % (net, service, str(x)))
            for product in self.products:
                for x in range(1,6):
                    start_urls.append(('https://www.shodan.io/search?query=net:%s'
                        '+product:%s&page=%s') % (net, product, str(x)))

    def init_request(self):
        print(self.nets)
        return scrapy.Request(url=self.login_page, callback=self.login)

    def login(self, response):
        return [scrapy.FormRequest.from_response(response,
                    formid='login-form',
		    #set your username and password
                    formdata={'username':self.username, 'password':self.password},
                    callback=self.after_login)]

    def after_login(self, response):
        if "invalid username or password" in response.body:
            self.log("Login failed", level=log.ERROR)
            return
        else:
            self.log('authentication succeed')
        return self.initialized()

    def parse(self, response):
        print response.xpath('id("search-results")/div/div[2]/div[2]/div[1]/a/text()').extract()
        print response.xpath('id("search-results")/div/div[2]/div[1]/text()').extract()
        for result in response.xpath('//div[@class="span9"]/div[@class="search-result"]/div/a[@class="details"]/@href'):
            url = response.urljoin(result.extract())
            print(result.extract())
            yield scrapy.Request(url, callback=self.parse_details_contents)

    def parse_details_contents(self, response):
        for details in response.xpath('//li[@class="service service-long"]'):
            item = SpydanItem()
            item['ip'] = response.xpath('//html/body/div[3]/div/div[2]/div/div[1]/div/h2/text()').extract()
            item['port'] = details.xpath('.//div[@class="port"]/text()').extract()
            item['protocol'] = details.xpath('.//div[@class="protocol"]/text()').extract()
            item['state'] = details.xpath('.//div[@class="state"]/text()').extract()
            head3 = details.xpath('.//div[@class="service-main"]/h3/text()').extract()
    	    hname = response.xpath('/html/body/div[3]/div/div[2]/div/div[1]/table/tbody/tr[6]/th/text()').extract()
    	    if hname:
    		item['hostname'] = hname
    	    else:
    		item['hostname'] = ''
            if head3:
                item['h3'] = head3
            else:
                item['h3'] = ''
            item['pre'] = details.xpath('.//div[@class="service-main"]/pre/text()').extract()
            yield item
