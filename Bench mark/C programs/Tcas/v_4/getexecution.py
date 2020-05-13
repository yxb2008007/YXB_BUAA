import numpy as np
import pickle
case_number=1578
execution_matrix=np.zeros((1578,174))
for i in range(1,case_number+1):
   file_tmp=open("cov_t"+str(i),"r")
   for line in file_tmp:
      if line[0:9]!="        -":
         if line[0:9]=="    #####":
                 execution_matrix[i-1,int(line[11:15])-1]=0
         else:
                 execution_matrix[i-1,int(line[11:15])-1]=1
   file_tmp.close()
file_test=open("matrix.txt","w")
pickle.dump(execution_matrix,file_test)
file_test.close
