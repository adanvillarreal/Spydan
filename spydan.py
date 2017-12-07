import sys
import argparse
import os
from time import gmtime, strftime

CLI = argparse.ArgumentParser(description='Extracts results from shodan.io')
CLI.add_argument(
    'user',
    help = 'Username used in shodan.io',

)
CLI.add_argument(
    'pswd',
    help = 'Password used in shodan.io',

)
CLI.add_argument(
    'nets',
    nargs = '+',
    help = 'Networks to query in shodan.io; e.g. 10.0.0.0/8 131.178.0.0/16',

)
CLI.add_argument(
    '--ports',
    nargs = '+',
    help = 'Ports to filter; e.g. 80 8080',
    default = []

)
CLI.add_argument(
    '--services',
    nargs = '+',
    help = 'Services to filter; e.g. RDP HTTP',
    default = []
)

CLI.add_argument(
    '--products',
    nargs = '+',
    help = 'Products to filter; e.g. Cisco, MySQL',
    default = []
)
CLI.add_argument(
    '--type',
    help = 'Output type (json, csv, xml)',
    default = 'csv'
)
CLI.add_argument(
    '--fname',
    help = 'Output filename',
    default = strftime("%Y%m%d%H%M%S", gmtime())
)
args = CLI.parse_args()
print (args)


#scrapy crawl someSpider -o some.json -t json 2> some.text


command = ('scrapy crawl spydan -a username="%s" -a password="%s" -a products="%s" -a nets="%s" -a ports="%s" -a services="%s" -o %s.%s') % (args.user, args.pswd, args.products, args.nets, args.ports, args.services, args.fname, args.type)
print (command)
os.system(command)
