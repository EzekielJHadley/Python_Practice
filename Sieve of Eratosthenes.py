# -*- coding: utf-8 -*-
"""
Created on Thu Nov 6
Last update 
@author: Thamor999
"""
"""
This program takes in a list of number from 2 to any value
assuming they are in order
and uses the Sieve of Eratosthenes to find the primes
"""

from sys import argv
from os.path import exists

#First i check to see if i offer alternate input output files
if len(argv) == 1:
	inputName = "input.csv"
	outputName = "output.csv"
else:
	script, inputName, outputName = argv
	
#output the files i am reading and writting to
print "The io files are: ", inputName, "and", outputName

#open the read and write files
inputFile = open(inputName)
outputFile = open(outputName, 'w') #'w' so i can write to it

#get the numbers to be strained
data = inputFile.read()

#now separate the numbers out into a list
data = data.split(',') #the values should be comma separated
#convert the strings to integers
values = [int(num) for num in data]

#initialise the list of primes
prime = []

while True:
	#the first number is obviously prime
	prime.append(values.pop(0))
	
	#check to make sure i still have values
	if(len(values) == 0):
		break
	
	#convert it to a set to compare to the set of multiples of out current prime
	valueSet = set(values)
	mult = set([prime[-1]*n for n in range(1, int(values[-1]/prime[-1])+1)]) #maxValue/prime + 1 ensures all possible multiples are found
	#remove the multiples
	valueSet = valueSet.difference(mult)
	values = list(valueSet)
	values.sort() #in-case set rearranges it (which it will)
	
		
#now convert the list of primes to a string

primeChar = [str(num) for num in prime]
line = ",".join(primeChar)
#output to the file
outputFile.write(line)

#now close the files
inputFile.close()
outputFile.close()