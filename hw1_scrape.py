#!/usr/bin/env python

import urllib2
import sys
import json
from bs4 import BeautifulSoup, NavigableString
import re
import csv
import datetime
import os
import time

def download_fromweb(link):
	data = []
	print link
	soup = BeautifulSoup(urllib2.urlopen(link).read(), from_encoding="utf-8")
	table = soup.find(lambda tag: tag.name=='table')
	rows = table.findAll(lambda tag: tag.name=='tr')
	
	downloaded = open("downloadedtable.csv", "w")
	downloadedwriter = csv.writer(downloaded)
	
	for row in rows:
		cleanrow =  row.get_text()
		cleanrow = cleanrow.encode("latin-1")
		cleanrow = cleanrow.split("\n")
		downloadedwriter.writerow(cleanrow[1:])
		
link = "http://www.archives.gov/federal-register/electoral-college/2012/popular-vote.html"
download_fromweb(link)

