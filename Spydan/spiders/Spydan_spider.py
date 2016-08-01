import scrapy
import csv
import sys
from scrapy.spiders.init import InitSpider
from scrapy.utils.response import open_in_browser
from scrapy.http.cookies import CookieJar
from Spydan.items import SpydanItem
import selenium
from selenium import webdriver

class LoginSpider(InitSpider):
    name = 'Spydan'
    login_page = 'https://account.shodan.io/login'
    services = ['mysql', 'cisco', 'webadmin', 'joomla', 'wordpress', 'vmware', 'tandberg', 'oracle', 'snmp', 'ntp', 'ssh']
    products = ['VNC', 'MySQL']
    ports = ['3389', '3306', '445', '137', '80', '81', '88', '8000', '8001', '8080', '8081', '22', '443', '21', '5900', '5901', '1433', '1521', '7001', '161', '123', '5060', '5061']
    inquery = 'https://www.shodan.io/search?query='
    nets = ['net:200.34.186.0/23','net:132.254.0.0/19','net:200.34.188.0/24','net:200.34.190.0/23','net:132.254.112.0/21','net:132.254.232.0/24','net:200.34.185.0/24','net:200.34.106.0/24','net:132.254.120.0/21','net:200.34.110.0/23','net:132.254.72.0/21','net:200.36.240.0/21','net:132.254.104.0/21','net:132.254.96.0/21','net:200.34.152.0/24','net:132.254.64.0/21','net:132.254.128.0/21','net:132.254.192.0/20','net:200.36.224.0/20','net:200.34.96.0/23','net:200.34.98.0/23','net:132.254.56.0/21','net:200.34.108.0/23','net:148.241.224.0/20','net:148.241.96.0/20','net:200.34.100.0/22']
    start_urls = []
    x = 0;
    for net in nets:
        for port in ports:
            for x in range(1,6):
                start_urls.append(inquery+net+'&page='+str(x)+'+port:"'+port+'"')
    for url in start_urls:
        print url
    def init_request(self):
        return scrapy.Request(url=self.login_page, callback=self.login)

    def login(self, response):
        return [scrapy.FormRequest.from_response(response,
                    formid='login-form',
                    formdata={'username': '', 'password': ''},
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
            yield scrapy.Request(url, callback=self.parse_details_contents)

    def parse_details_contents(self, response):

        for details in response.xpath('//li[@class="service service-long"]'):
            item = SpydanItem()
            item['ip'] = response.xpath('//html/body/div[3]/div/div[2]/div/div[1]/div/h2/text()').extract()
            item['port'] = details.xpath('.//div[@class="port"]/text()').extract()
            item['protocol'] = details.xpath('.//div[@class="protocol"]/text()').extract()
            item['state'] = details.xpath('.//div[@class="state"]/text()').extract()
            head3 = details.xpath('.//div[@class="service-main"]/h3/text()').extract()
            if head3:
                item['h3'] = head3
            else:
                item['h3'] = 'NOT AVAILABLE'
            item['pre'] = details.xpath('.//div[@class="service-main"]/pre/text()').extract()
            yield item
