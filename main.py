#!/usr/bin/python

from src.trello2Email import trello2Email


apikey = 'your api key'
tocken = 'your trello tocken'
boardId = 'id of trello board you are interested in'
TO = 'rec@gmail.com'
FROM ='snd@gmail.com'
subject = 'subject'
trello2Email(apikey,tocken,boardId,TO,FROM,subject)