# # featre selection include or exclude the features but in dimensionality we merg the existing featiure to made new feature to reduce the number of the features 




# # this is called feature selection method not the dimensionality reduction 
# from sklearn.feature_selection import SelectKBest,chi2,mutual_info_classif,SelectPercentile,SelectFpr #fpr select on the false positive rate
# from sklearn.datasets import load_breast_cancer
# x,y = load_breast_cancer(return_X_y=True)
# bc = load_breast_cancer()
# x1,y1 = bc.data,bc.target

# print(x.shape)
# kChi= SelectKBest(chi2,k=15).fit_transform(x,y)

# print(kChi.shape)
# perChi = SelectPercentile(chi2,percentile=15).fit_transform(x,y)
# print(perChi.shape)
# result = bc.feature_names
# perMu = SelectPercentile(mutual_info_classif,percentile=15).fit(x1,y1)
# kChi2_selector = SelectKBest(chi2, k=4)
# kChi2 = kChi2_selector.fit_transform(x1, y1)
# print("Selected features (K=4, chi2):", result[kChi2_selector.get_support()])

# print(result[kChi2.get_support()])
# transMu = perMu.transform(x1)
# # print(result[perMu.get_support()])
# # print(result)


from sklearn.feature_selection import SelectKBest, chi2, mutual_info_classif, SelectPercentile,SelectFpr
from sklearn.datasets import load_breast_cancer

# Load data
x, y = load_breast_cancer(return_X_y=True)
bc = load_breast_cancer()
x1, y1 = bc.data, bc.target

print("Original shape:", x.shape)

# Using SelectKBest with chi2
kChi_selector = SelectKBest(chi2, k=15)
kChi = kChi_selector.fit_transform(x, y)
print("SelectKBest shape:", kChi.shape)

# Using SelectPercentile with chi2
perChi = SelectPercentile(chi2, percentile=15).fit_transform(x, y)
print("SelectPercentile (chi2) shape:", perChi.shape)

# Using SelectPercentile with mutual_info_classif
perMu = SelectPercentile(mutual_info_classif, percentile=15).fit(x1, y1)

# Using SelectKBest again with chi2 for 4 best features
kChi2_selector = SelectKBest(chi2, k=4)
kChi2 = kChi2_selector.fit_transform(x1, y1)
result = bc.feature_names
# FPR 
fprSelector = SelectFpr(chi2, alpha=0.01)
fpr = fprSelector.fit_transform(x1, y1)
print("Selected features Based on FPR ", result[fprSelector.get_support()])
# Get feature names of selected features

# print("Selected features (K=4, chi2):", result[kChi2_selector.get_support()])

# If you want to also print mutual info selected features
# print("Selected features (15% mutual info):", result[perMu.get_support()])
