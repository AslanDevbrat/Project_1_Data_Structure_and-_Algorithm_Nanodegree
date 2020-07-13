"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

set1=set()
#print(type(set1))

for lists in texts:         #O(n)
    set1.add(lists[0])      #O(1)
for lists in texts:         #O(n)
    set1.add(lists[1])      #O(n)
#print("text count=",len(set1))    

set2=set()
for list in calls:          #O(n)
    set2.add(list[0])       #O(1)
for list in calls:          #O(n)
    set2.add(list[1])       #O(1)
#print("call count=",len(set1))

different_numbers= set()

for list in set2:           #O(n)
    set1.add(list)          #O(1)
print("There are ",len(set1)," different telephone numbers in the records.")    
    
    

