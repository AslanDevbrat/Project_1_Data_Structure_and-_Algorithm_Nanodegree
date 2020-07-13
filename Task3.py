"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)
    

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
set_landLine_area_code=set()    #O(1)
set_phone_area_code= set()      #O(1)
set_telemarket_code= set()      #O(1)
i=0                             #O(1)
for list in calls:                          #O(n)
    if list[0].find("(080)") is not -1:
        #print(list[0],"called",list[1])
        if list[1].partition("(")[2].partition(")")[0] is not "":
            set_landLine_area_code.add(list[1].partition("(")[2].partition(")")[0])
        else:
            if list[1].find(" ") is not -1 :
                set_phone_area_code.add(list[1][0:4])
            elif list[1].startswith("140")  :
                set_telemarket_code.add(list[1])
                #print("Unknown Number",list[1])
                # print("phone",list[1],"code",m)
#print(set_landLine_area_code)
#print(set_phone_area_code)
taskA_area_code = set_landLine_area_code.union(set_phone_area_code)
""" 
    To sort on the basis of integer value 
    convert the set to 
    integer list un commenting the following
    line by following line.
    
    """
#taskA_area_code= {int(x) for x in taskA_area_code}
#print(taskA_area_code)

taskA_area_code=sorted(taskA_area_code)
#print(taskA_area_code)
print(set_telemarket_code)
print("The number called by people in Bangalore have codes:")
for item in taskA_area_code:
    print(item)
   
"""Task B""" 
total_outgoing_calls_from_bangalore=0   
count=0 
for list in calls:
    if list[0].startswith("(080)") :
        total_outgoing_calls_from_bangalore+=1
        if list[1].startswith("(080)"):
            count+=1
print(count)  
percentage=(count/total_outgoing_calls_from_bangalore)*100      
#print((count/len(calls))*100," percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")     
print("{:.2f}  percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percentage, 2)))