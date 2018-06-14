#!usr/bin/python
num = int(input("Enter any no. : "))

fac = 1
i = 1

while i <= num:
 fac = fac * i
 i = i + 1

print "Factorial of", num , " is ", fac
