#!/usr/bin/python

from cStringIO import StringIO

def getHtmlFromBuf(bufList, bufCard, cadNumber):
	buf = StringIO()
	buf.write('Bonjour,')
	buf.write('<body>')
	j = 0
	k = 0
	for lis in bufList:
		buf.write('<h3>' + lis + '</h3>')
		for i in range(cadNumber[j]):
			buf.write('<li>' + bufCard[k] + '</li>')
			k = k+1
		j = j+1
	buf.write('</body>')
	return buf.getvalue() 

