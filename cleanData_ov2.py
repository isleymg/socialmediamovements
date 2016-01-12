import os
import csv
import re

'''
What this chunk of code does: 
-----------------------------
This opens each of the tweetFile<month>.txt files, and parses through them to append 
relevant information (tweet text, tweet hashtags, and created at date) to lists

'''



# change this to the folder on your computer where you're keeping the text files
os.chdir('C:\\Users\\Isley\\Anaconda\\socialmediamovements\\textfiles')


tweets=[]
tweetsjune = []
tweetsjuly = []
tweetsaugust = []
tweetssep = []

created_at = []

nums = [261217, 40569, 261217, 17447, 1406486, 236367]

# tweetFileAll.txt must not have all the tweets - need to fix that
f = open("tweetFileMay.txt", "r")
for line in f.readlines():
    tweets.append(line.split('*~^..^?'))

tweets = tweets[0]
num_tweets=int(tweets[0])


created_at = tweets[1].split(",")
remove = ["u\'", "\'", "[", "]"]
for x in remove:
    created_at = [w.replace(x, '') for w in created_at]
created_at = [w.lstrip() for w in created_at]

text = tweets[2].split('+~^..^?')
text = text[:-1] #remove bracket from end
remove = ["u\"", "u\'", "[", "]", "\",", "\',"]
for x in remove:
    text = [w.replace(x, '') for w in text]
text = [w.lstrip() for w in text]


user = tweets[4].split(',')
user[0] = user[0].replace("[","")
user[num_tweets-1] = user[num_tweets-1].replace("]","")

hashtags = tweets[14].split('], [')
'''removes clutter from hashtags, currently doesn't work because MemoryError'''
hashtags = tweets[14].split('], [')
remove = ["u\'", "[", "]", "\'"]
for x in remove:
    hashtags = [w.replace(x, '') for w in hashtags]


# list of strings, some are multiple. convert to list of lists :3 
f.close()

print("done May")

f = open("tweetFileJune.txt", "r")
for line in f.readlines():
    tweetsjune.append(line.split('*~^..^?'))

tweetsjune = tweetsjune[0]
num_tweets += int(tweetsjune[0])


created_at.extend(tweetsjune[1].split(","))
remove = ["u\'", "\'", "[", "]"]
for x in remove:
    created_at = [w.replace(x, '') for w in created_at]
created_at = [w.lstrip() for w in created_at]

text.extend(tweetsjune[2].split('+~^..^?'))
text = text[:-1] #remove bracket from end
remove = ["u\"", "u\'", "[", "]", "\",", "\',"]
for x in remove:
    text = [w.replace(x, '') for w in text]
text = [w.lstrip() for w in text]

user.extend(tweetsjune[4].split(','))
user[0] = user[0].replace("[","")
user[num_tweets-1] = user[num_tweets-1].replace("]","")

hashtags.extend(tweetsjune[14].split('], ['))
hashtags = tweets[14].split('], [')
remove = ["u\'", "[", "]", "\'"]
for x in remove:
    hashtags = [w.replace(x, '') for w in hashtags]


f.close()
print("done June")

f = open("tweetFileJuly.txt", "r")
for line in f.readlines():
    tweetsjuly.append(line.split('*~^..^?'))

tweetsjuly = tweetsjuly[0]
num_tweets += int(tweetsjuly[0])

created_at.extend(tweetsjuly[1].split(","))
remove = ["u\'", "\'", "[", "]"]
for x in remove:
    created_at = [w.replace(x, '') for w in created_at]
created_at = [w.lstrip() for w in created_at]

text.extend(tweetsjuly[2].split('+~^..^?'))
text = text[:-1] #remove bracket from end
remove = ["u\"", "u\'", "[", "]", "\",", "\',"]
for x in remove:
    text = [w.replace(x, '') for w in text]
text = [w.lstrip() for w in text]

user.extend(tweetsjuly[4].split(','))
user[0] = user[0].replace("[","")
user[num_tweets-1] = user[num_tweets-1].replace("]","")

hashtags.extend(tweetsjuly[14].split('], ['))

f.close()
print("done July")


f = open("tweetFileAugust.txt", "r")
while 1:
    line = f.readline()
    if not line:
        break
    else:
        tweetsaugust.append(line.split('*~^..^?'))

    
    
for line in f.readlines():
    tweetsaugust.append(line.split('*~^..^?'))

tweetsaugust = tweetsaugust[0]
num_tweets += int(tweetsaugust[0])

created_at.extend(tweetsaugust[1].split(","))
remove = ["u\'", "\'", "[", "]"]
for x in remove:
    created_at = [w.replace(x, '') for w in created_at]
created_at = [w.lstrip() for w in created_at]

text.extend(tweetsaugust[2].split('+~^..^?'))
text = text[:-1] #remove bracket from end
remove = ["u\"", "u\'", "[", "]", "\",", "\',"]
for x in remove:
    text = [w.replace(x, '') for w in text]
text = [w.lstrip() for w in text]

user.extend(tweetsaugust[4].split(','))
user[0] = user[0].replace("[","")
user[num_tweets-1] = user[num_tweets-1].replace("]","")

hashtags.extend(tweetsaugust[14].split('], ['))

f.close()
print("done August")


f = open("tweetFileSeptember.txt", "r")

while 1:
    line = f.readline()
    if not line:
        break
    else:
        tweetssep.append(line.split('*~^..^?'))


tweetssep = tweetssep[0]
num_tweets += int(tweetssep[0])

created_at.extend(tweetssep[1].split(","))
remove = ["u\'", "\'", "[", "]"]
for x in remove:
    created_at = [w.replace(x, '') for w in created_at]
created_at = [w.lstrip() for w in created_at]
text.extend(tweetssep[2].split('+~^..^?'))
text = text[:-1] #remove bracket from end
remove = ["u\"", "u\'", "[", "]", "\",", "\',"]
for x in remove:
    text = [w.replace(x, '') for w in text]
text = [w.lstrip() for w in text]

user.extend(tweetssep[4].split(','))
user[0] = user[0].replace("[","")
user[num_tweets-1] = user[num_tweets-1].replace("]","")
user = [w.replace(" ", '') for w in user]

hashtags.extend(tweetssep[14].split('], ['))
remove = ["u\'", "[", "]", "\'"]
for x in remove:
    hashtags = [w.replace(x, '') for w in hashtags]
hashtags = [w.lstrip().lower().split(',') for w in hashtags]

f.close()
print("done Sep")



'''Takes each of the lists for hashtags, text, and created_at, and writes into a different text file'''

with open('cleanDataHashtags-test1.txt', 'wb') as results:
    for eachlist in hashtags:
        results.write(str(eachlist)+"\n")


with open('cleanDataText-test1.txt', 'wb') as textResults:
    for each in text:
        textResults.write(str(each) + "\n")

with open('cleanDataDate-test1.txt', 'wb') as dateResults:
    for each in created_at:
        dateResults.write(str(each) + "\n")
        
