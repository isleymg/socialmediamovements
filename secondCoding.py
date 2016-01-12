'''
OVERVIEW OF secondCoding.py
-------
This script executes secondCoding_Overlaps.py.

Then it opens the pairsdict and dictlist files outputted by secondCoding_Overlaps.py, 
and goes through the below script to take out tweet samples based on the coding sheet provided by Oliver. 
A more detailed explanation is below at line 90. 

This script finally outputs two csv files that contain the tweet samples for movements with overlap and movements without overlap. 
'''

import os
import random
from collections import defaultdict
import csv

os.chdir('C:\\Users\\Isley\\Anaconda\\socialmediamovements\\textfiles')

'''Executes the secondCoding_clean.py'''
execfile('C:\\Users\\Isley\\Anaconda\\socialmediamovements\\secondCoding_Overlaps.py')
print("START")

'''A list of each of the movement pairs in 2tuples'''
movtuples = [('nmos14', 'ferguson'), ('yesallmen', 'yesallwhitewomen'), ('icantbreathe', 'ericgarner'), ('nmos14', 'blacklivesmatter'), ('nmos14', 'mikebrown'), ('nmos14', 'icantbreathe'), ('cisgaze', 'yesallmen'), ('nmos14', 'iftheygunnedmedown'), ('notallmen', 'ferguson'), ('handsupdontshoot', 'mikebrown'), ('handsupdontshoot', 'ferguson'), ('handsupdontshoot', 'iftheygunnedmedown'), ('yesallwomen', 'notallmen'), ('handsupdontshoot', 'ericgarner'), ('yesallwomen', 'ferguson'), ('ericgarner', 'blacklivesmatter'), ('yesallmen', 'yesallwomen'), ('mikebrown', 'icantbreathe'), ('yesallmen', 'yesallpeople'), ('yesallwhitewomen', 'yesallpeople'), ('handsupdontshoot', 'icantbreathe'), ('yesallpeople', 'yesallwomen'), ('translivesmatter', 'yesallwomen'), ('yesallwhitewomen', 'yesallwomen'), ('blacklivesmatter', 'ferguson'), ('cisgaze', 'yesallwomen'), ('translivesmatter', 'blacklivesmatter'), ('iftheygunnedmedown', 'ferguson'), ('cisgaze', 'yesallpeople'), ('nmos14', 'nativelivesmatter'), ('heforshe', 'yesallwomen'), ('mikebrown', 'ferguson'), ('nmos14', 'handsupdontshoot'), ('heforshe', 'notallmen'), ('iftheygunnedmedown', 'yesallwomen'), ('yesallmen', 'notallmen'), ('yesallwhitewomen', 'notallmen'), ('mikebrown', 'ericgarner'), ('iftheygunnedmedown', 'blacklivesmatter'), ('ericgarner', 'ferguson'), ('handsupdontshoot', 'blacklivesmatter'), ('cisgaze', 'yesallwhitewomen'), ('mikebrown', 'iftheygunnedmedown'), ('mikebrown', 'blacklivesmatter'), ('translivesmatter', 'ferguson'), ('icantbreathe', 'blacklivesmatter'), ('yesallpeople', 'notallmen'), ('iftheygunnedmedown', 'ericgarner'), ('icantbreathe', 'ferguson'), ('nmos14', 'ericgarner'), ('ericgarner', 'yesallwomen'), ('ericgarner', 'notallmen'), ('yesallmen', 'icantbreathe'), ('icantbreathe', 'heforshe'), ('yesallpeople', 'ferguson'), ('cisgaze', 'ericgarner'), ('cisgaze', 'notallmen'), ('handsupdontshoot', 'nativelivesmatter'), ('mikebrown', 'translivesmatter'), ('nmos14', 'cisgaze'), ('cisgaze', 'ferguson'), ('heforshe', 'yesallwhitewomen'), ('handsupdontshoot', 'yesallwhitewomen'), ('cisgaze', 'icantbreathe'), ('cisgaze', 'blacklivesmatter'), ('yesallwomen', 'nativelivesmatter'), ('yesallmen', 'ericgarner'), ('iftheygunnedmedown', 'heforshe'), ('cisgaze', 'nativelivesmatter'), ('iftheygunnedmedown', 'cisgaze'), ('yesallwhitewomen', 'ferguson'), ('yesallwhitewomen', 'translivesmatter'), ('heforshe', 'nativelivesmatter'), ('notallmen', 'nativelivesmatter'), ('heforshe', 'blacklivesmatter'), ('blacklivesmatter', 'notallmen'), ('mikebrown', 'heforshe'), ('mikebrown', 'yesallwomen'), ('nmos14', 'yesallwhitewomen'), ('iftheygunnedmedown', 'notallmen'), ('ericgarner', 'nativelivesmatter'), ('iftheygunnedmedown', 'yesallmen'), ('iftheygunnedmedown', 'yesallwhitewomen'), ('yesallpeople', 'nativelivesmatter'), ('nmos14', 'yesallwomen'), ('yesallpeople', 'blacklivesmatter'), ('iftheygunnedmedown', 'nativelivesmatter'), ('translivesmatter', 'notallmen'), ('yesallwhitewomen', 'ericgarner'), ('nmos14', 'translivesmatter'), ('blacklivesmatter', 'yesallwomen'), ('icantbreathe', 'notallmen'), ('ericgarner', 'translivesmatter'), ('nativelivesmatter', 'ferguson'), ('nmos14', 'yesallpeople'), ('handsupdontshoot', 'translivesmatter'), ('heforshe', 'ferguson'), ('cisgaze', 'heforshe'), ('nmos14', 'notallmen'), ('blacklivesmatter', 'nativelivesmatter'), ('handsupdontshoot', 'cisgaze'), ('icantbreathe', 'yesallpeople'), ('heforshe', 'yesallpeople'), ('icantbreathe', 'translivesmatter'), ('icantbreathe', 'yesallwomen'), ('yesallwhitewomen', 'blacklivesmatter'), ('heforshe', 'translivesmatter'), ('yesallmen', 'heforshe'), ('mikebrown', 'cisgaze'), ('mikebrown', 'yesallwhitewomen'), ('icantbreathe', 'yesallwhitewomen'), ('nmos14', 'heforshe'), ('translivesmatter', 'nativelivesmatter'), ('ericgarner', 'yesallpeople'), ('nmos14', 'yesallmen'), ('icantbreathe', 'nativelivesmatter'), ('handsupdontshoot', 'yesallpeople'), ('iftheygunnedmedown', 'icantbreathe'), ('yesallmen', 'ferguson'), ('mikebrown', 'notallmen'), ('mikebrown', 'yesallmen'), ('handsupdontshoot', 'heforshe'), ('handsupdontshoot', 'yesallwomen'), ('cisgaze', 'translivesmatter'), ('heforshe', 'ericgarner'), ('handsupdontshoot', 'yesallmen'), ('yesallmen', 'blacklivesmatter'), ('handsupdontshoot', 'notallmen'), ('iftheygunnedmedown', 'yesallpeople'), ('yesallmen', 'translivesmatter'), ('yesallwhitewomen', 'nativelivesmatter'), ('mikebrown', 'nativelivesmatter'), ('yesallmen', 'nativelivesmatter'), ('iftheygunnedmedown', 'translivesmatter'), ('yesallpeople', 'translivesmatter'), ('mikebrown', 'yesallpeople')]

#THESE ARE NOW RUN INSIDE secondCoding_clean.py, SO IT IS UNNECESSARY TO HAVE THE SAME FILES RE-OPENED IN THIS SCRIPT. 
#THE COMMENTED CODE CAN BE DELETED, BUT ARE STILL HERE JUST FOR REFERENCE.
# '''The file openers below open said files (which were initially created by cleanData_ov2.py) and reads them into lists'''
# # Opens cleanDataText-test1.txt as a list of tweet text content
# with open('cleanDataText-test1.txt','r') as cleanDataText:
#     text = []
#     while 1:
#         line = cleanDataText.readline()
#         if not line:
#             break
#         else:
#             text.append(line)
# print('Tweet Text IMPORTED')

# # Opens cleanDataHashtags-test1.txt as a list of tweet hashtags
# import ast
# with open('cleanDataHashtags-test1.txt', 'r') as cleanDataResults:
#     hashtags = []
#     while 1:
#         line = cleanDataResults.readline()
#         if not line:
#             break
#         else:
#             line = line.translate(None, "[]' \n")
#             tempList = line.split(',')
#             hashtags.append(tempList)

# print('Hashtags IMPORTED')

# # Opens cleanDataDate-test1.txt as a list of tweet created_at dates
# with open('cleanDataDate-test1.txt','r') as cleanDataDate:
#     created_at = []
#     while 1:
#         line = cleanDataDate.readline()
#         if not line:
#             break
#         else:
#             created_at.append(line)
# print('Created At Dates IMPORTED')

'''Opens files (outputted by secondCoding_clean.py)'''
'''SecondOverlapResults-counts is opened and assigned to variable pairsdict.
   pairsdict is a dictionary with each movement tuple as a key and the count of total overlaps for that tuple as the value'''
with open('SecondOverlapResults-counts.txt', 'r') as soResults:
    secondOverlap = soResults.readline()
    pairsdict = ast.literal_eval(secondOverlap)\
print('Second Overlap Results (pairsdict) IMPORTED')

'''SecondOverlapResults-dictionary is opened and assigned to variable dictlist.
   dictlist is a dictionary with each movement tuple as a key and a list of tuples (user, [list of tweet indexes]) as the value'''
with open('SecondOverlapResults-dictionary.txt', 'r') as dictListResults:
    try:
        dictstuff = dictListResults.readline()
        dictlist = ast.literal_eval(dictstuff)
    except (SyntaxError, ValueError):
        pass
print("DictList IMPORTED")


'''Initializes two defaultdicts for where overlaps were found and where they were NOT found, respectively'''
second_overlap = defaultdict(list)
non_second_overlap = defaultdict(list)


'''
What this chunk of code does:
-----------------------------
for every tuple in the list of movement tuples (for example: ('heforshe', 'blacklivesmatter')), 
    the first hashtag is the 0th index, the second hashtag is the 1st index
    if the count of overlaps for that tuple is not zero and less than 6, get as many tweet sets as there exists in that tuple
        append to the corresponding tuple key in second_overlap
    if the count of overlaps for that tuple is not zero and greater than 6, get 6 tweet sets in that tuple
        append to the corresponding tuple key in second_overlap
    if the count of overlaps for that tuple is zero, then get 9 tweets from each hashtag in that tuple
        append to the corresponding tuple key in non_second_overlap

'''
num = 0     #A counter so that you can tell how far along it has gotten to finshing running
for ntuple in movtuples:
    hash0 = ntuple[0]
    hash1 = ntuple[1]
    if pairsdict[ntuple] !=0 and pairsdict[ntuple] <6:
        mov1indices6 = []
        mov2indices6 = []
        for usertuple in dictlist[ntuple]:
            tweetslist = usertuple[1]
            for tweetindex in tweetslist:
                if hash0 in hashtags[tweetindex]:
                    mov1indices6.append(tweetindex)
                if hash1 in hashtags[tweetindex]:
                    mov2indices6.append(tweetindex)

            for i in range(pairsdict[ntuple]):
                randomu1 = random.choice(mov1indices6)
                randomu2 = random.choice(mov2indices6)
                u = (text[randomu1], created_at[randomu1])
                u2 = (text[randomu2], created_at[randomu2])
                second_overlap[ntuple].append((u, u2))

    if pairsdict[ntuple] !=0 and pairsdict[ntuple] >= 6:
        mov1indices = []
        mov2indices = []
        for usertuple in dictlist[ntuple]:
            tweetslist = usertuple[1]
            for tweetindex in tweetslist:
                if hash0 in hashtags[tweetindex]:
                    mov1indices.append(tweetindex)
                if hash1 in hashtags[tweetindex]:
                    mov2indices.append(tweetindex)

        for i in range(6):
            randomx1 = random.choice(mov1indices)
            randomx2 = random.choice(mov2indices)
            x = (text[randomx1], created_at[randomx1])
            x2 = (text[randomx2], created_at[randomx2])
            second_overlap[ntuple].append((x, x2))

    if pairsdict[ntuple] == 0 : # No overlap, pick 9 from each movement
        mov1indicesNon = []
        mov2indicesNon = []
        for i in range(len(hashtags)):
            if hash0 in hashtags[i]:
                mov1indicesNon.append(i)
            if hash1 in hashtags[i]:
                mov2indicesNon.append(i)
        for i in range(9):
            randomy1 = random.choice(mov1indicesNon)
            randomy2 = random.choice(mov2indicesNon)
            y = (text[randomy1], created_at[randomy1])
            y2 = (text[randomy2], created_at[randomy2])
            non_second_overlap[ntuple].append(y)
            non_second_overlap[ntuple].append(y2)

    print('{} out of {} completed'.format(num, len(movtuples))) #Progress bar that you will see as this script runs
    num += 1 #Increment
        
            
        
print("Writing to file")
'''Writes the dictionary of second_overlap into a csv file'''
writer = csv.writer(open('secondDictSamplesTRUE.csv', 'wb'))
for key, value in second_overlap.items():
    for tweettuple in value:
        writer.writerow([key, tweettuple[0][0], tweettuple[0][1], tweettuple[1][0], tweettuple[1][1]])

'''Writes the dictionary of non_second_overlap into a csv file'''
writer2 = csv.writer(open('secondDictSamplesFALSE.csv', 'wb'))
for key, value in non_second_overlap.items():
    for singletweet in value:
        writer2.writerow([key, singletweet[0], singletweet[1]])


print("Finished")
