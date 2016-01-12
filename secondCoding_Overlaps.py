'''
OVERVIEW OF secondCoding_Overlaps.py
-------
This script opens files containing all of the tweet text, tweet hashtags, and created by dates, 
and assigns each to variables as lists.

It also opens a file containing every user and that user's tweets in the form of the index. 
A tweet with index 111 will have the hashtags of hashtags[111] and text[111], created at created_at[111].

This script outputs pairsdict and dictlist, which are used in secondCoding.py to take samples.
'''

import os
import csv
import re
import itertools
from collections import defaultdict
import random

# change this to the folder on your computer where you're keeping the text files
os.chdir('C:\\Users\\Isley\\Anaconda\\socialmediamovements\\textfiles')
movements = {'yesallwomen', 'yesallwhitewomen', 'cisgaze', 'notallmen', 'yesallmen', 'heforshe', 'yesallpeople', 'ferguson', 'handsupdontshoot', 'icantbreathe', 'nmos14', 'iftheygunnedmedown', 'ericgarner', 'mikebrown', 'blacklivesmatter', 'nativelivesmatter', 'translivesmatter'}
    
'''Creates a list of all possible pairwise combinations of hashtags
   and initializes a dictionary with combinations as keys and zero as items'''

pairsdict = {} #Set that contains all counts, initialized at zero 
dictlist = {}
for subset in itertools.combinations(movements,2):
    pairsdict[subset] = 0
    dictlist[subset] = []


print('At dictionaries')
'''The file openers below open said files (which were initially created by cleanData_ov2.py) and reads them into lists'''
# Opens cleanDataText-test1.txt as a list of tweet text content
import ast
with open('cleanDataHashtags-test1.txt', 'r') as cleanDataResults:
    hashtags = []
    while 1:
        line = cleanDataResults.readline()
        if not line:
            break
        else:   
            line = line.translate(None, "[]' \n")
            tempList = line.split(',')
            hashtags.append(tempList)

# Opens cleanDataHashtags-test1.txt as a list of tweet hashtags
with open('cleanDataText-test1.txt','r') as cleanDataText:
    text = []
    while 1:
        line = cleanDataText.readline()
        if not line:
            break
        else:
            text.append(line)
print('Tweet Text IMPORTED')

# Opens cleanDataDate-test1.txt as a list of tweet created_at dates
with open('cleanDataDate-test1.txt','r') as cleanDataDate:
    created_at = []
    while 1:
        line = cleanDataDate.readline()
        if not line:
            break
        else:
            created_at.append(line)
print('Created At Dates IMPORTED')


#Opens allDicts.txt as the dictionary to be parsed.
#allDicts.txt is a dictionary with user ID as the key and [usertweetindexes] as the value
with open('allDicts.txt','r') as allDictsFile:
    allDicts = allDictsFile.readline()
    dictionary = ast.literal_eval(allDicts)
print('allDicts PARSED')

'''
This chunk of code goes through the allDicts.txt dictionary and parses it so that it outputs two files:
    1. pairsdict, which is a dictionary {(hashtag0, hashtag1): count}
    2. dictlist, which is a dictinoary of {(hashtag0, hashtag1): [('userID':[tweetindexes])}

'''
num = 0
for user in dictionary:
    print("USER: {} out of {}".format(num, len(dictionary.keys())))
    num += 1
    usertweetslist = dictionary[user]
    
    for tweetindex in usertweetslist:
        hashset = set(hashtags[tweetindex])
        hashset = hashset.intersection(movements)
        if len(hashset) > 1:
            for tweettuple in itertools.combinations(hashset, 2):
                if tweettuple in pairsdict.keys():
                    pairsdict[tweettuple] += 1
                    dictlist[tweettuple].append((user, usertweetslist))
                elif (tweettuple[1],tweettuple[0]) in pairsdict.keys():
                    pairsdict[tweettuple[1],tweettuple[0]] += 1
                    dictlist[tweettuple[1],tweettuple[0]].append((user, usertweetslist))

with open('SecondOverlapResults-counts.txt', 'wb') as results:
    results.write(str(pairsdict))

with open('SecondOverlapResults-dictionary.txt', 'wb') as resultslist:
    resultslist.write(str(dictlist))

print('Finished')
        



