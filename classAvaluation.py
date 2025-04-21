import numpy as np  

# a = np.array([11,12,13,14,15,16,17,18,19,20])
# for i in range(3):
#     print(a[i])

# a[9] = 100
# print(a) 

# q2
id = np.array([1,2,3,4,5,6,7,8,9,10])
print(id[0:10:2])

id[0:10:2] = 100#yes it change the array 
print(id[0:10:2])
print(id)


# q3
threeByThree = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(threeByThree[1,2])
id2 = [threeByThree[0,1] , threeByThree[1,1] , threeByThree[2,1]]
id5 = threeByThree[:,1]
print(id5)
print(id2)
# q4
# 
rangedArray = np.linspace(0,49,50)
identity = np.identity(3)
print(rangedArray)
Random = np.zeros([4,2])
for i in range(4):
    for j in range(2):
        Random[i,j] = rangedArray[i+j]
print(Random.shape)
print(Random.size)
print(Random.ndim)
# q5
id3 = np.linspace(0,0,5)
for i in range(5):
    id3[i] = i+1
print(id3)
# q6
arr = np.array([8,2,5,1,7])
sorted = np.sort( arr)
print(sorted)
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(np.concatenate((array1,array2)))

# q7
size = np.array([1,2,3,4,5,6])
sizeNew = np.reshape(size,(2,3))
print(size[np.newaxis,:])
print(sizeNew)
print(size)
to2d = np.expand_dims(size,axis=1)
print(to2d)

