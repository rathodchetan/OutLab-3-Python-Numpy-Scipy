import scipy.integrate
#from scipy import integrate
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('a', type=float)
parser.add_argument('b', type=float)
parser.add_argument('c', type=float)
parser.add_argument('d', type=float)
parser.add_argument('e', type=float)
parser.add_argument('f', type=float)

args = parser.parse_args()
result,err=scipy.integrate.nquad(lambda x,y,z:(x**2)*(y**2)*(z**2),[[args.a,args.b],[args.c,args.d],[args.e,args.f]])
print(result)

