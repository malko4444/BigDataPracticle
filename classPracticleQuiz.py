import numpy as np
c = np.empty([2,2,2,4],dtype=np.int64)
s = np.array([[[[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]], [[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]]], 
[[[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]], [[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]]]])
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(4):
                # c[i,j,k,l] =s[i,j,k,l]+ s[i,j,k,l]+1
                if((s[i,j,k,l])%2 == 0):
                    c[i,j,k,l] = s[i,j,k,l]+1
                else:
                    c[i,j,k,l] = s[i,j,k,l]

print(c)