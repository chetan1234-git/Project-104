import csv 

with open('newData.csv') as f : 
    reader=csv.reader(f)
    a = list(reader)

a.pop(0)
newData = []

for i in range(len(a)) :
    b = a[i][2]
    newData.append(float(b))

n = len(newData)
t = 0

for x in newData :
    t+=x

mean = t/n
print('Mean of the data is '+ str(mean))

