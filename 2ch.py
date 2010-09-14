#!/usr/bin/env python

import urllib2, gzip, StringIO
import re
import time
from BeautifulSoup import BeautifulSoup

url="http://news2.2ch.net/" #2ch url
now = int(time.time())

def get_thread_list(subject):
	threads = []
	patarn = "(\d+)\.dat<>(.+)\s\((\d+)\)"
	for line in subject:
		m = re.search(patarn,unicode(line))
		thre={
			"datnum":int(m.group(1)),
			"title":unicode(m.group(2),'shift-jis').encode('utf-8'),
			"res":int(m.group(3)),
			"pow":res/float(now-datnum)*86400
		}
		threads.append(thre)
	return threads

def get_dat(host,board, datnum):
	txdata="GET /"+board+"/dat/"+datnum+".dat HTTP/1.0"
	txheaders={
		'Accept-Encoding':'gzip',
		'Host':host,
		'User-Agent':'Monazilla/1.00',
		'Connection':'close'
	}
	req = urllib2.Request(url, txdata, txheaders)
	

def get_subject(host,board):
    txurl='http://'+host
    txdata='GET /'+board+'/subject.txt HTTP/1.1'
    txheaders={
		'Accept-Encoding':'gzip',
		'Host':host,
		'User-Agent':'Monazilla/1.00',
		'Connection':'close'
	}
    req = urllib2.Request(txurl,txdata,txheaders)

def get_board_list():
    txurl='http://menu.2ch.net/bbstable.html'
    txdata='GET HTTP/1.1'
    txheaders={
        'Accept-Encoding':'gzip',
        'Host':'menu.2ch.net',
        'User-Agent':'Monazilla/1.00',
        'Connection':'close'
	}
    req = urllib2.Request(txurl,txdata,txheaders)
    r= urllib2.urlopen(req)
    if( r.code != 200 ):
    	return None
    body = r.read()
    #decod gzip
    if( r.info().getheaders('Content-Encoding')[0] == 'gzip'):
    	sf=StringIO.StringIO(body)
        dec=gzip.GzipFile(fileobj=sf)
        body=dec.read()
    return body
    """
    result = []
    patarn = "<A HREF=(.+\.2ch\.net)/(.+)/ TARGET=_blank>(.+)</A>"
    m=re.search(patarn,body)
    return m
    """
"""
    res={
        'host':m.group(1),
        'board':m.group(2),
        'board_title':m.group(3)
    }
    result.append(res)
	return result
"""

if __name__=='__main__':
    url="http://menu.2ch.net"
    body = get_board_list()

    bs = BeautifulSoup(body)
    links=bs.findAll('a', href=re.compile('.+\.2ch\.net'))
    for i in links:
        print i
#    print body.decode('shift-jis')
