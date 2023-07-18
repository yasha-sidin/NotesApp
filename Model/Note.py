import datetime

class Note():
    id = 0
    date_of_creation = ''
    header = 'dddd'
    body = ''

    def __init__(self, id, header, body):
        self._header = header
        self._body = body
        self._date_of_creation = datetime.datetime.now()
        self._id = id

    def getid(self):
        return self._id

    def getheader(self):
        return self._header

    def setheader(self, header):
        self._header = header

    def getbody(self):
        return self._body

    def setbody(self, body):
        self._body = body

    def getdate_of_creation(self):
        return self._date_of_creation

    id = property(getid)
    date_of_creation = property(getdate_of_creation)
    header = property(getheader, setheader)
    body = property(setbody, getbody)

