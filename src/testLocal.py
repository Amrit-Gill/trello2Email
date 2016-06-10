#!/usr/bin/python

from trello import TrelloApi
from cStringIO import StringIO
import smtplib
import getHtml
import htmlEmailTest
import datetime



# tocken trello
apikey = 'your api key'
tocken = 'your trello tocken'


trello = TrelloApi(apikey)
trello.set_token(tocken)

# board id
boardId = 'id of trello board you are interested in'

cards = trello.boards.get_card(boardId, fields=("name", "idList"))
lists = trello.boards.get_list(boardId)

bufList = StringIO()
bufCard = StringIO()
boardLists = []
boardcard = []
cadNumber = []

lis = 0
for list in trello.boards.get_list(boardId):
	member_card = dict()
	listName = list['name']
	bufList.write(listName.encode('utf-8'))
	boardLists.append(bufList.getvalue())
	bufList.truncate(0)
	lis = lis + 1

	for card in trello.lists.get_card(list['id']):
		for member in card['idMembers']:
			if not member_card.has_key(member):
				member_card[member] = []
			member_card[member].append(card)
	cad = 0
	for memberId in member_card.keys():
		member = trello.members.get(memberId)
		for card in member_card[memberId]:
			cardName = card['name']
			memberInitials = member['initials']
			bufCard.write(memberInitials.encode('utf-8') + ' : ' + cardName.encode('utf-8'))
			boardcard.append(bufCard.getvalue())
			bufCard.truncate(0)
			cad = cad + 1
	cadNumber.append(cad)

html = getHtml.getHtmlFromBuf(boardLists, boardcard, cadNumber)
print('Email Sent.!')

TO = 'rec@gmail.com'
FROM ='snd@gmail.com'
today = datetime.date.today()
subject = today.strftime('Subject : %d, %b %Y')
htmlEmailTest.py_mail(subject, html, TO, FROM)
