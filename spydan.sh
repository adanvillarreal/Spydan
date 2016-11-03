#!/bin/bash
if [ "$1" != "" ]; then
	scrapy crawl Spydan -t csv -o $1.csv --loglevel=INFO
else
	now=$(date +"%s");
	scrapy crawl Spydan -t csv -o  $now.csv --loglevel=INFO
fi
