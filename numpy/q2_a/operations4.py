import numpy as np 
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--path', type=str, required=True)
# Parse the argument
args = parser.parse_args()

numpy_array = np.loadtxt(args.path,dtype=int,delimiter=',') 

unique_elements, counts_elements = np.unique(numpy_array, return_counts=True)
print(np.asarray(unique_elements)) 
print(np.asarray(counts_elements))  
i = np.unique(numpy_array)[-2]
print(np.count_nonzero(numpy_array == i))  
