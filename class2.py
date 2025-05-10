import numpy as np
a = np.array([[[1, 2, 3, 4, 5],[3, 4, 5, 6, 7],[3,3,3,4,6]]])  
b = np.array([[3, 4, 5, 6, 7],[3, 4, 5, 6, 7]])
# c  = np.concatenate((a,b))
print(a.size) #size is 15
# size must be same when e apply the reshape method 
reshaped = a.reshape(5,3)
print("the reshap array ",reshaped)#%*3=15

# print(c.reshape(1,1))  
# axis 1 mean colum wise concate .get the first aray and concate it with teh second array and add the second array of forst and add ot woth the second array of the second array . dose not  matter  the size matter the entries as well
print("******************************")
# c  = np.concatenate(((a,b)axis=1))
# print(c)  
# know change the current shape of the array but the condition is size is same 
# difficult to convert the dimension when the dimension have all the odd values like (3,3,3) a even value have more option to reduce the dimmensionality 




addDimension = np.array([3, 4, 5, 6, 7])
print("the dimension",addDimension[np.newaxis,:].shape)#add the new dimension withe the (1,5)
print(addDimension[:np.newaxis].shape)#add the new dimension withe the (5,1)
print("the new dimension",np.expand_dims(addDimension,axis=0).shape)#new dimension also added by this 