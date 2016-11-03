Spydan is a spider created with scrapy which crawls shodan.io in order to extract the results from the search engine. 

BEFORE YOU START CRAWLING:
You will need to install scrapy. This can be achieved by running:
	$ pip install scrapy
If you want to know more about scrapy, go to scrapy.org.
You will need to set a valid shodan.io username and password in the def login located in Spydan_spider.py, line 38.

SUGGESTIONS:
Because shodan.io restricts free users to 5 pages of results (circa 50 results), I strongly suggest to be as specific as possible in your queries in such a way that you get less than 5 pages of results so that you can get the most of this tool. You can modify the query in line 28, and the parameters in the lists from line 15 to 18 (feel free to add more if needed).
There is a shell script that runs the spider and outputs the results in a .csv. This script takes as an argument the name for the .csv output file. If no argument is provided, the script will assign a name with the time of execution. In order to run this script, enter:
	$ ./spydan.sh output_file_name 
Anyways, if you want to run the scrapper from the terminal for debugging or other reasons, you can enter:
	$ scrapy crawl spydan
Finally, I have set a delay between downloads of 3 seconds and a limit of concurrent requests of 2 as I was getting 503 codes from the details pages. Feel free to tweak this values, which are located at the settings.py file in lines 30 and 32.
Feel free to let me know any concerns, questions or recommendations. 

Created by Adan Villarreal.
