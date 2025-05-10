import numpy as np



arr = np.array([
    [[2,3,4,5,5,6],
     [4,5,6,7,8,9],
     [5,6,7,8,9,10]
    ],
    [[3,4,5,6,7,8],
     [5,6,7,8,9,0],
     [6,7,8,9,0,1]]
    ])
arr1 = np.array([ [1,2,3,4,5],
                  [6,7,8,9,0],
                  [1,2,3,4,5],
                  [6,7,8,9,0]
                ])
# print(arr1)
zerosArray = np.zeros((2,4,4,4),dtype=int)
emptyArray = np.empty((2,4,4,4),dtype=int)
# print(emptyArray)
# print(zerosArray)
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.itemsize)#per item size like 32 bit mean 4 bytes
# print("number of butes ",arr.nbytes)#total size of array in bytes
# print(arr[1,0,3])


# arrange = np.arange(2,20,3)
# print(arrange)
# linespace = np.linspace(2,20,12)
# print(linespace)


# sort the array 
# a = np.array([3,4,6,"x",832,2,5,80,"A"])
# sortArray = np.sort(a,kind="mergesort")
# print("original array ",a)
# argSoert = np.argsort(a)#gave the index 
# # print(argSoert)
# print(sortArray)
# emptyArray = np.empty((4,4,4,4))
# # print(emptyArray)
# for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             for l in range(4):
#                 emptyArray[i,j,k,l] = i*j*k*l
# print(emptyArray)
# x = np.array([
#     [3,4,5],
#     [6,7,8]
#     ])
# y = np.array([[9,10],
            #   [12,13]
            #   ])
# z = np.concatenate((x,y),axis=0)# zero mean increase the row and 1 mean it increase/ add it in colum 
# z1 = np.concatenate((x,y),axis=1)# zero mean increase the row and 1 mean it increase/ add it in colum 

# print(z.shape)
# print(z1.shape)
# reshapArray = z.reshape(12,1)
# print(reshapArray)
# print(z.size)
# print(y.shape)
# print(y)
# y = np.expand_dims(y,axis=0)
# print(y.shape)
# print(y)


from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.feature_selection import f_classif, chi2, SelectKBest,SelectPercentile,SelectFpr, mutual_info_classif
# x,y = load_iris(return_X_y=True)
# print(x.shape)
# k_chi = SelectKBest(chi2,k=5).fit_transform(x,y)
# print("the before fit transform ",k_chi)

# print("selected featire ", k_chi.shape)
# mutualClass = SelectKBest(mutual_info_classif, k= 5).fit_transform(x,y)
# print(mutualClass.shape)
# usePercentile = SelectPercentile(mutual_info_classif, percentile=1).fit_transform(x,y)

# print(usePercentile.shape)



# select = SelectKBest(score_func=f_classif,k=2).fit_transform(x,y)
# print("the selected feature ",select.shape)


# fpr = SelectFpr(score_func=chi2, alpha=0.02).fit_transform(x,y)
# print("fpr",fpr.shape)

bc = load_breast_cancer()
X,Y = bc.data, bc.target
featureName = bc.feature_names
# print(featureName)
print(X.shape)

usingseparate = SelectPercentile(mutual_info_classif, percentile=5).fit_transform(X,Y)
# trans = usingseparate.transform(X)
print("the direct ",usingseparate.shape)
# print(featureName[usingseparate.get_support()])

withMutualClassIf = SelectKBest(chi2, k=5).fit_transform(X,Y)
# transformed = withMutualClassIf.transform(X)
print(withMutualClassIf.shape)

# print(featureName[withMutualClassIf.get_support()])



# Use Case	Method to Use
# Fit and transform on same data	fit_transform()
# Fit on train and transform on test	fit() then transform()






















# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_breast_cancer, load_iris, load_wine, load_digits
# from sklearn.feature_selection import SelectKBest, chi2, mutual_info_classif, SelectPercentile, SelectFpr,GenericUnivariateSelect,SelectFdr,SelectFwe
# from sklearn.metrics import accuracy_score,mean_absolute_error,mean_squared_error
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import LogisticRegression,LinearRegression
# from sklearn.svm import SVC
# from sklearn.naive_bayes import GaussianNB
# from sklearn.neighbors import KNeighborsClassifier

# a= np.array([[[1,2,3],[4,5,6]],
#             [[3,2,3],[4,2,6]],
#             [[17,4,5],[9,3,6]],
#             [[9,2,3],[4,5,7]],
#             [[5,3,2],[2,6,8]]])
# print(a)

# tips = sns.load_dataset("tips")
# sns.boxplot(x="day", y="total_bill", data=tips)
# plt.xlabel("Days ")
# plt.ylabel("Total ($)")
# plt.title("Boxplot of total bill amounts by day")
# plt.show()

# from sklearn.feature_selection import SelectKBest, chi2
# from sklearn.datasets import load_breast_cancer


# X, y = load_breast_cancer(return_X_y=True)

# k_chi=SelectKBest(mutual_info_classif, k=8).fit_transform(x, y)
# print(k_chi.shape)





