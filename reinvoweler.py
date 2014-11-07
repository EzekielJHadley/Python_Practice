# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14
Last update Fri Aug 15
@author: Thamor999
"""

from sys import argv
from os.path import exists

#First i check to see if i offer alternate input output files
if len(argv) == 1:
	inputName = "input.txt"
	outputName = "output.txt"
else:
	script, inputName, outputName = argv
	
#State what files i will be inputting and outputting from
print "The io files are:", inputName, "and", outputName, "\n"

#i will be reading from the output of the disinvoweler2
#then comparing to its input
inputFile = open(outputName)
compareFile = open(inputName)
#retrieve the vowel-less text
txt = inputFile.readline()
#retrieve the vowels
vowels = inputFile.readline()
#now get the line I will be comparing
original = compareFile.read()

#i need to strip the carrage return from the two strings
txt = txt.strip("\n")
vowels = vowels.strip("\n")

print txt
print vowels

#i'm going to brute force this and turn the strings into lists
txtList = []
vowelList = []
for i in range(len(txt)):
	txtList.append(txt[i])
	vowelList.append(vowels[i])

for i in range(len(txtList)):
	if txtList[i] == " ":
		print i, ":", txtList[i], "-->", vowelList[i]
		txtList[i] = vowelList[i]

#now convert it back into a string
txt = "".join(txtList)
		
#now compare
print "Did it work? (t/f): ", txt == original

print txt
print original
print vowels

inputFile.close()
compareFile.close()