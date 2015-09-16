import sys
import datetime

def main(startTime, endTime):
	date_now = datetime.datetime.now()

	startHour = int(startTime.split(":")[0])
	startMinute = int(startTime.split(":")[1])
	endHour = int(endTime.split(":")[0])
	endMinute = int(endTime.split(":")[1])
	
	start_time = datetime.datetime(date_now.year, date_now.month, date_now.day, startHour, startMinute, 00)
	end_time = datetime.datetime(date_now.year, date_now.month, date_now.day, endHour, endMinute, 00)

	hours = abs(start_time - end_time).total_seconds() / 3600.0

	print "Total: %.2f hours\n" % hours

if __name__=="__main__":
	if len(sys.argv) != 3:
		print "Error: python hours_worked.py <start:time> <end:time>\n"
	else:
		main(sys.argv[1], sys.argv[2])
