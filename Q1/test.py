startResults = [0,11,16,28]
endResults = [15,20,25,35]
startCount = 1
endCount = 0
posEnd = 0
match = 0
if (len(startResults) == 1):
	print(endResults[posEnd])
else:
	while (startCount<len(startResults) and match>=0):
		if (startResults[startCount] < endResults[endCount]):
			startCount+=1
			posEnd+=1
			match+=1
		else:
			endCount+=1
			match -=1
	if (startCount >= len(startResults)):
                # We got to the end of the list
		print(endResults[len(endResults)-1])
	else:
		print(endResults[posEnd])
                    
