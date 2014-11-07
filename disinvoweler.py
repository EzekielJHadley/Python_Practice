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
print "The io files are:", inputName, "and", outputName

#open the files and then read the text from the input file
inputFile = open(inputName)
outputFile = open(outputName, 'w')
text = inputFile.read()

#display what the initial text is
print text

	#hard code all the various vowels, both upper and lower
	#vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
	#i don't need this because i can use the dictionary for the same thing
#create a dictionary to hard code the vowels
#and to keep track of how many of each are removed
vowelCount = { 	'A' : 0,
				'a' : 0,
				'E' : 0,
				'e' : 0,
				'I' : 0,
				'i' : 0,
				'O' : 0,
				'o' : 0,
				'U' : 0,
				'u' : 0
			}
#start the read head at the beginning of the string
i = 0

#now lets just loop until I hit the end of the string
while True:
	#if the current value in the string is in the vowel dictionary
	if text[i] in vowelCount:
		#increment that entry
		vowelCount[text[i]] += 1
		#then replace it with nothing
		text = text.replace(text[i], "", 1)
	else:
		#it isn't a vowel move the read head over one
		i += 1
	
	#once the read head has moved past the end stop the loop
	#this works because the length is always the location + 1
	if( i == len(text)):
		break

#now print the vowel-less text and the vowel count
print text
print vowelCount

#also write it to the output file along with the vowels removed and their quantity
outputFile.write(text + "\n")
outputFile.write("The following vowels where removed, and their quantity \n")
for i in vowelCount:
	if vowelCount[i] > 0:
		line = i + " : %r \n" % vowelCount[i]
		outputFile.write(line)

#close out the files when done
inputFile.close()
outputFile.close()