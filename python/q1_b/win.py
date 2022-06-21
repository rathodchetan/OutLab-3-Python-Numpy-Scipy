import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--path1', type=str, required=True)
parser.add_argument('--path2', type=str, required=True)
parser.add_argument('--output', type=str, required=True)

args = parser.parse_args()


file1=open(args.path1) 
lines = file1.readlines()
for line in lines:
  v=line.lstrip("https://")   
  #v=line.lstrip("/") 
  #v=line.split("/")
  u=v.split(".")
  z=u[2].split("/")  
  print(u[0]+"."+u[1]+"."+z[0].rstrip())  
  
file2=open(args.path2)      
lines2 = file2.readlines()  
save_path = args.output
completeName = os.path.join(save_path, "winner.txt")          
file3 = open(completeName, "w")


count = 0
for line in lines:  
   for line2 in lines2: 
        u=line2.split("||")  
        user_name = u[0] 
        IP_address = u[2]
        url_complete=line
        if(line == u[3] or line.lstrip("https://")==u[3] or line.lstrip("https://www.")==u[3]):
              count +=1 
              w = f"user_name - {user_name} : Winner - Lucky draw!!! - {url_complete}"  
              file3.write(f"{user_name}||{IP_address}||{url_complete}")   
              print(w)
print(count) 
