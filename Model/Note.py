import datetime

class Note():
    def __init__(self, id, header, body):
        self._header = header
        self._body = body
        self._date_of_creation = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self._id = id
        self._date_of_last_update = ''

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

    def setdate_of_creation(self, date_of_creation):
        self._date_of_creation = date_of_creation

    def getdate_of_creation(self):
        return self._date_of_creation

    def getdate_of_last_update(self):
        return self._date_of_last_update

    def setdate_of_last_update(self, date):
        self._date_of_last_update = date

    def __str__(self):
        return f"note: {{id: {self._id}, creation_date: {self._date_of_creation}, last_update: " \
               f"{self._date_of_last_update}, header: {self._header}}}"

    id = property(getid)
    date_of_creation = property(getdate_of_creation, setdate_of_creation)
    header = property(getheader, setheader)
    body = property(setbody, getbody)
    date_of_last_update = property(getdate_of_last_update, setdate_of_last_update)


