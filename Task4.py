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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
set_telemarket_number = set()
set_calls_outgoing,set_calls_incoming,set_text_send,set_text_recieved = set(),set(),set(),set()

for list in calls:                      #O(n)
    set_calls_outgoing.add(list[0])     #O(1)
    set_calls_incoming.add(list[1])     #O(1)
for list in texts:                      #O(n)
    set_text_send.add(list[0])          #O(1)
    set_text_recieved.add(list[1])      #O(1)
set_telemarket_number=set_calls_outgoing-set_calls_incoming-set_text_send-set_text_recieved
print("These numbers could be telemarketers: ")
for element in sorted(set_telemarket_number):   #O(n)
    print(element)                              #O(1)