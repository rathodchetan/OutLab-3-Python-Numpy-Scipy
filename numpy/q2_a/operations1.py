import numpy as np 
import argparse
# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--path', type=str, required=True)
# Parse the argument
args = parser.parse_args()

arr = np.loadtxt(args.path,dtype=int,delimiter=',')  
lv=range(arr.shape[0])
for a in lv:
	i = 0
	while i<=a:
		print(arr[i,a],end=' ');
		i=i+1
	print('\n')
