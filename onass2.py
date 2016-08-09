#finding the year in which age will be 100 years
import datetime
get = datetime.datetime.now()
try:
	name = raw_input("Enter your name: ")
	age = raw_input("Enter your age: ")
	age = int(age) 
	pin = raw_input("Enter your area zipcode: ")
	yr = get.year	
	hundyr = (100 - age)+yr

	print "Hello Mr/Mrs. %s.\nyou will turn 100 years old in the year %s.\nyour area's pincode is %s" %(name,hundyr,pin)
except:
	print "Please enter valid data"