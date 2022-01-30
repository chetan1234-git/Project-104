import csv 
from collections import Counter

with open('newData.csv') as f : 
    reader=csv.reader(f)
    a = list(reader)

a.pop(0)
newData = []

for i in range(len(a)) :
    b = a[i][2]
    newData.append(float(b))

data = Counter(newData)
mRange = {'50-60':0,'60-70':0,'70-80':0}

for height,occurence in data.items() :
    if 50 < float(height) < 60 :
        mRange['50-60']+=occurence 
    elif 60 < float(height) < 70 :
        mRange['60-70']+=occurence 
    elif 70 < float(height) < 80 : 
        mRange['70-80']+=occurence 

modeRange, modeOccurence = 0,0 

for range, occurence in mRange.items() :
    if occurence>modeOccurence:
        modeRange,modeOccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((modeRange[0]+modeRange[1])/2)

print('Mode of the data is '+ str(mode))

