import numpy as np 
# Import the library
import argparse
# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--path', type=str, required=True)
parser.add_argument('--num', type=str, required=True)
# Parse the argument
args = parser.parse_args()
 
numpy_array = np.loadtxt(args.path,dtype=int,delimiter=',') 
num=args.num
a = np.pad(numpy_array, pad_width=int(num), mode='constant')
print(a) 
