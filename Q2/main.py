"""
I have noted that a parser cannot be used to finish this question as the Declaration tag lacks an ending tag
Therefore I've added a python script which parses this data as is, and then changed the document to include an ending and parsed through that
Hopefully these scripts are what you are looking for.

"""
# Script using An XML Parser

import xml.etree.ElementTree as ET

root = ET.parse('testfileAltered.xml').getroot()
results = {}
itemsToFind = set({})
itemsToFind.add("MWB")
itemsToFind.add("TRV")
itemsToFind.add("CAR")
for reftext in root.iter():
    if reftext.get("RefCode") in itemsToFind:
        results[reftext.get("RefCode")] = reftext
refTextList = []
for i in itemsToFind:
    refTextList.append(results[i])
    # print(results[i].findall('RefText')[0].text)

#Script using python
results = {}
results["TRV"] = None
results["MWB"] = None
results["CAR"] = None

def getSubstring(textStart,info):
    start = info[textStart:].find('RefText')+textStart+8
    end = info[start:].find("<")
    information = info[start:start+end]
    return information

with open("testfile.txt") as file: # Use file to refer to the file object
   data = file.read()
   reftext1start = data.find('RefCode="MWB"')+1
   print(getSubstring(reftext1start,data))
   reftext2start = data.find('RefCode="TRV"')+1
   print(getSubstring(reftext2start,data))
   reftext3start = data.find('RefCode="CAR"')+1
   print(getSubstring(reftext3start,data))
