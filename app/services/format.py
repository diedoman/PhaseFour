import datetime
def strDateFormat(date):
	if type(date) is datetime.datetime:
		return str(date.year) + "-" + str(date.month) + "-" + str(date.day) + "_" + str(date.hour) + ":" + str(date.minute) 
	else:
		print(type(date))
