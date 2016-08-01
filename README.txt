Spydan is a spider created with scrapy which crawls shodan.io in order to extract the results from the search engine. 

BEFORE YOU START CRAWLING:
You will need to install scrapy. This can be achieved by running:
	$ pip install scrapy
If you want to know more about scrapy, go to scrapy.org.
You will need to set a valid shodan.io username and password in the def login located in Spydan_spider.py, line 35.

SUGGESTIONS:
Because shodan.io restricts free users to 5 pages of results (circa 50 results), I strongly suggest to be as specific as possible in your queries in such a way that you get less than 5 pages of results. If it is not possible, you can divide your queries. 
Another strong suggestion I have is to output the results into a .csv, this will allow you to better analyze and organize the output. To achieve this, you need to cd into the spiders folder and run:
	$ scrapy crawl Spydan -t csv -o FILENAME.csv --loglevel=INFO
Finally, you can modify the queries. Shodan.io allows you to search for ports, services, products, and more. You can modify the search query in the for-loop on line 23 of Spydan_spider.py. The query itself is on line 26. 

Created by Adan Villarreal.
