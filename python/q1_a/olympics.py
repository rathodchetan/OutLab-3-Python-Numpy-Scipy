import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--path', type=str, required=True)

args = parser.parse_args()


myDict = {}

path =args.path
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))


for name in filelist:
	with open(name) as f:
		for line in f:
			txt=line.split("-")
			for i in [1,2,3]:
				txt[i]=int(txt[i])
			if txt[0] in myDict.keys():
				a=myDict[txt[0]]
				b=[txt[1],txt[2],txt[3]]
				c = [a[i] + b[i] for i in range(len(a))]
				myDict[txt[0]]=c
			else:
				myDict[txt[0]]=[txt[1],txt[2],txt[3]]

Sdi=sorted(myDict.items(), key=lambda t: t[::-1],reverse=True)
print(myDict)
print(Sdi)

i=0
while i<len(Sdi)-1:
	j=i+1
	if Sdi[i][1][0] == Sdi[j][1][0]:
		while j<len(Sdi)-1 and Sdi[i][1][0] == Sdi[j+1][1][0]:
			j=j+1	
		for k in range(i,j+1):
			for m in range(k+1,j+1):
				if Sdi[k][0]>Sdi[m][0]:
					a=Sdi[k]
					Sdi[k]=Sdi[m]
					Sdi[m]=a		
	i=j
	
print(dict(Sdi))

