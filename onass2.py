#manipulating strings
#finding the year in which age becomes 100 years
import datetime
get = datetime.datetime.now()
try:
	name = raw_input("Enter your name: ")
	age = raw_input("Enter your age: ")
	age = int(age) 
	times = raw_input("How many times you want to print: ")
	ntimes = int(times)
	yr = get.year	
	turn100 = (100 - age)+yr

	print (ntimes*("Hello Mr/Mrs. %s.you will turn 100 years old in the year %s.\n"%(name,turn100)))
except:
	print "Please enter valid data"