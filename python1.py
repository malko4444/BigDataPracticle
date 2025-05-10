import numpy as np
# # implicit and explicit 
# #  assigning a value in ana array while defining is called explicit and its alternate the implicite 
# b = np.zeros([2,2,2,3],dtype=np.int64)
# # print(b) 
# a = np.ones([2,2,2,3],dtype=np.int64)
# # print(a) 
# # empty array 
# c = np.empty([2,2,2,3]) 
# # empty get the any value bydefault and it change on every time when the program is  executed 
# print(c) 


# # arrnge method normally generated the one dimensional array 
# e = np.arange(2,15,2) #range the one dimensional array of 2 to 15 while the 3rd is for gap between them
# # print(e)
# # linespace 
# l = np.linspace(2,15) #generater the 100 
# # print(l)
# w = np.linspace(2,15,3) #generater on the basis on 3rd arguments 
# # print(w)




# # for sorting the array 
# s = np.array([[[[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]], [[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]]], 
# [[[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]], [[3,8,2,4],[2,7,9,3],[1,2,3,4],[9,1,2,4]]]])
# # in sort method the bydefault its quiksort we can change the sorting type  by using the kind method 
# print(np.sort(s,kind="mergsort"))#sort inside the each array 
# print(np.argsort(s))#sort in the argument wise 

from sklearn.datasets import load_wine
from sklearn.feature_selection import chi2, SelectPercentile
x,y = load_wine(return_X_y=True)
print(x.shape)
feture = SelectPercentile(chi2, percentile=50).fit_transform(x,y)
print(feture.shape)