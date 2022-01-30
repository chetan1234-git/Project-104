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
newData.sort()

if n%2==0 :
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median = (median1+median2)/2
else :
    median=(newData[n//2])
    
print('Median of the data is '+ str(median))

