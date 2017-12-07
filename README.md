# Spydan
A web spider for [shodan.io](https://www.shodan.io)

## What can you do?
Spydan allows you to retrieve information from shodan.io without an API Key and export it as CSV, JSON or XML by creating queries with given parameters. 

Due to the five page limit Shodan has for standard users, the results are limited to those shown in these first pages.

## Getting Started

### Prerequisites
Before you start crawling, you need to have [Scrapy](https://scrapy.org/)
```
pip install scrapy
```
### Usage
You only need to worry about the file `spydan.py`. You will need to add some arguments when running Spydan. The required ones are username password and networks. Other arguments are ports, services and products.

A full example is:
```
python spydan.py adanvillarreal p455w0rd 131.178.0.0/16 148.241.128.0/18 --ports 80 8080 8084 8484 --fname prueba --type json

```

You can get more information about arguments by executing
```
python spydan.py -h
```

## Tweaking
There is a delay between requests of 3 seconds and a limit for 2 concurrent requests due to 503 codes that I received with higher values, which are located in `settings.py` under the directory spydan.
## Author
Adan Villarreal

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

