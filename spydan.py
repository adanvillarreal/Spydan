import sys
import argparse
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
    help = 'Services to filter; e.g. mysql http',
    default = []

)
CLI.add_argument(
    '--type',
    help = 'Output type (JSON, CSV, XML)',
    default = 'CSV'
)
CLI.add_argument(
    '--fname',
    help = 'Output filename',
    default = strftime("%Y-%m-%d-%H:%M:%S", gmtime())
)
args = CLI.parse_args()
print (args)
fileout = args.fname
if args.type == 'CSV':
    fileout = fileout + '.csv'
elif args.type == 'JSON':
    fileout = fileout + '.json'
else:
    fileout = fileout + '.xml'

command = ('scrapy crawl Spydan -a user=%s -a password=%s -a nets=%s --output '
    '%s -a ports=%s -a services=%s') % (args.user, args.pswd, args.nets, fileout, args.ports, args.services)
print (command)
