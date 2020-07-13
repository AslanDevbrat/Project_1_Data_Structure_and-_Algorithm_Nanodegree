"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from operator import itemgetter, attrgetter
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
phone_dictionary={}

for list in calls:                      #O(n)
    #print(list)
    if list[0] in phone_dictionary:
        phone_dictionary[list[0]]+= int(list[3])
    else:
        phone_dictionary[list[0]]=int(list[3])
    if list[1] in phone_dictionary:
        phone_dictionary[list[1]]+= int(list[3])
    else:
        phone_dictionary[list[1]]=int(list[3])

        
    
phone_dictionary=sorted(phone_dictionary.items(), key=lambda item: item[1],reverse=True)   #O(nlogn)
print(phone_dictionary[0][0], "spent the longest time, ",phone_dictionary[0][1],"seconds, on the phone during September 2016. " ) 
    
    

