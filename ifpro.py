#import commands
#commands.getoutput("date")ue 

#!usr/bin/python

import commands

print "enter commands : "
print "1. date"
print "2. calender"

value = raw_input("enter choice")

if value == "1":
	value1 = commands.getoutput("date")
	print value1

elif value == "2":
	value2 = commands.getoutput("cal")
	print value2

else :
	print "wrong choice"

#=====================================================================================


