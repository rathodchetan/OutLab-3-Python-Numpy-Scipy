import numpy as np 
import argparse

# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
parser.add_argument('--path', type=str, required=True)
# Parse the argument
args = parser.parse_args()
numpy_array = np.loadtxt(args.path,dtype=int,delimiter=',')  
print(numpy_array.mean(axis=0)) 
print(np.median(numpy_array,axis=0))     
x=np.std(numpy_array,axis=0)  
np.set_printoptions(precision=2)
np.array(x)       
print(x)

print(np.linalg.det(numpy_array))
numpy_array_inverse = np.linalg.pinv(numpy_array) 
np.set_printoptions(precision=2)
np.array(numpy_array_inverse) 
print(numpy_array_inverse) 

