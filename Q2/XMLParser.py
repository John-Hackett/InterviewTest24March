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
    print(results[i].findall('RefText')[0].text)
