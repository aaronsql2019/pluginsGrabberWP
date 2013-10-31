#!/usr/bin/env	python
# -*- config:utf-8 -*-

'''
  @author Verri Andriawan < cloud.and.ri@gmail.com >
  Created at Nov 1st, 2013

'''

import urllib2
import re
import sys
import os

try:
	from BeautifulSoup import BeautifulSoup
except:
	print "Module BeautifulSoup required.."

try:
	from termcolor import colored
except:
	print "Sorry termcolor need to install.."


if __name__ == '__main__':
	
	print "\nTry to grapping the plugins.."
	
	BUFF = 16384
	resp = urllib2.urlopen('http://plugins.svn.wordpress.org')
	line = 0

	with open('plugins.lst', 'w') as fp:

		try:
			while True:
				newr = resp.fp._sock.recv(2048)
				if not newr: break

				html = BeautifulSoup(newr)
				list = html.findAll('li')
				for li in list:
					try:
						line+=1
						glis = re.findall(r"<li.*><a.*>(.*)<\/a>", str(li))[0]
						nli = re.sub(r"/$",'',glis)
						print colored("["+str(line)+"] "+nli, "green")
						fp.write(nli+"\n")
					except:pass
		except: 
			print "Program force to closed..."
			sys.exit()

	print "\nTotal Current Plugins: " + colored(str(line), "red") + "\n"
	print "Finished.."
