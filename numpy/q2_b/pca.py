import numpy as np
import pandas as pd
from numpy import savetxt
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--path', type=str, required=True)
parser.add_argument('--output', type=str, required=True)

args = parser.parse_args()

arr=pd.read_csv(args.path,delimiter=',',header=None)
arr=arr.values
#print(arr)
arr_mean=np.mean(arr,axis=0)
#print(arr_mean)

#print(arr-arr_mean)

arr_std=arr-arr_mean
#print(arr_std)
arr_cov=np.dot(np.transpose(arr_std),arr_std)/(arr.shape[0])
#print(arr_cov.shape[0])
eigen_value,eigen_vector=np.linalg.eig(arr_cov)
#print(eigen_value)
#print(eigen_vector)
#print("----------------------")
eigen_value_sorted=np.sort(eigen_value)[::-1]
eigen_vector_sorted=eigen_vector[:,eigen_value.argsort()[::-1][:eigen_value.shape[0]]]
print(eigen_value_sorted)
#print(eigen_vector_sorted)
#print(arr_cov)		
		
k_eigen_vector=np.zeros((eigen_vector.shape[0],2))
for i in range(eigen_vector.shape[0]):
	for j in range(2):
		k_eigen_vector[i][j]=eigen_vector_sorted[i][j]

#print(k_eigen_vector)
transformed=np.dot(arr_std,k_eigen_vector)
#print(transformed)
savetxt(args.output+'transform.csv', transformed, delimiter=',')
#print(sys.argv[4])
x=transformed[:,0]
x=x.tolist()
y=transformed[:,1]
y=y.tolist()
plt.scatter(x,y,c="blue")
plt.xlim([-15, 15])
plt.ylim([-15, 15])
#plt.show()
plt.savefig(argsoutput+'out.png')


