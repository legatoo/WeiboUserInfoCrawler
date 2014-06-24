#!/bin/python

from pyquery import PyQuery as pq
from elementSetting import QUERY_INFO


# return HTML not wrapped by JavaScript
def generateHTML(page, query):
	lines = page.splitlines()
	doc = ''
	for line in lines:
		if line.startswith(query):
			pos = line.find('html":"')
			if pos > 0:
				line = line.decode('utf-8')
				try:
					line = eval("u'''" + line + "'''").encode('utf-8')
					_doc = line[pos+7:-12].decode('utf-8').replace('\/', '/')
				except:
					_doc = line[pos+7:-12].replace('\/', '/').replace('\\"', '"').replace("\\'", "'")
					_doc = _doc.replace('\\t', '').replace('\\n', '')
				doc += _doc + '\n'

	return doc

