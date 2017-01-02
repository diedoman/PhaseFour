import datetime
from app.services.format import strDateFormat

class Event:
	timestamp = 0
	def __init__(self):
		self.timestamp = datetime.datetime.now()
	def write(self):
		return strDateFormat(self.timestamp)
