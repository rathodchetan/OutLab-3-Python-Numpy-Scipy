import numpy as np 
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--path', type=str, required=True)
# Parse the argument
args = parser.parse_args()

numpy_array = np.loadtxt(args.path,dtype=int,delimiter=',')  
print(np.sort(numpy_array, axis=0))
print(np.sort(numpy_array, axis=1)) 
print(np.sort(numpy_array, axis=None)) 
