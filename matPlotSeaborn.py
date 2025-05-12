import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np
# air = pd.read_csv("air.csv")
# using pandas 
# # print(black.head())
# # black["station_london"].plot()
# air.plot.scatter(x="station_london", y="station_paris")
# air.plot.box()
# air.plot.area(figsize=(3,4),subplots=True)
# plt.show()


# now use the matplotlib to plot the data
# s for squeare ^ for triangle o for circle -- for dashed line
# plt.plot(air["station_london"], air["station_paris"],"r--")
# plt.plot([1,2,3,4,5],[2,3,4,0,6], "r--")
# plt.hist(air["station_london"],density=True, facecolor="g", histtype='bar' ,bins=10)
# plt.title("Histogram of station_london and station_paris")
# plt.xlabel("station_london")
# plt.ylabel("station_paris")
# plt.show()

groups = ["group1", "group2", "group3"]
values = [10, 20, 15]
# plt.figure(figsize=(8,9))
# plt.subplot(131)
# plt.bar(groups, values)
# plt.title("Bar Chart")
# plt.subplot(132)
# plt.scatter(groups, values)
# plt.title("Scatter Plot")
# plt.subplot(133)
# plt.hist(values, histtype='stepfilled', bins=1)
# plt.show()


# fig, axes = plt.subplots(2,2, figsize=(10, 8))
# fig.suptitle("Subplots Example", fontsize=16)
# axes[0,0].scatter(groups,values)
# axes[0,0].set_title("Scatter Plot")
# axes[0,1].bar(groups,values)
# axes[0,1].set_title("Bar Chart")
# axes[1,0].hist(values, histtype='stepfilled', bins=1)
# axes[1,0].set_title("Histogram")
# axes[1,1].plot(groups,values)
# axes[1,1].set_title("Line Plot")
# plt.show()
iris = load_iris()
# plt.hist(iris.data[:,2])
# plt.show()
# plt.show()
# import seaborn as sns
iris = sns.load_dataset("iris")
# mpg = sns.load_dataset("mpg")
# tips = sns.load_dataset("tips")
# data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # print(data)
# coolwarm
# viridis
# magma
# YlOrRd
# RdBu
# Blues
# Greens
# sns.heatmap(data, annot=True,cmap="RdBu")

# plt.title("Heatmap Example")
# plt.show()
# sns.boxplot(x="day", y="total_bill", data=tips)
# plt.title("Boxplot Example")
# plt.show()
# plt.subplot(1, 2, 1)
# sns.pairplot(iris, hue="species")
# print(iris.columns)
# plt.title("Pairplot Example")
# plt.subplot(1, 2, 2)
# sns.pairplot(iris)
# plt.show()
# sns.barplot(x="day", y="total_bill", data=tips)
# plt.title("Barplot Example")
# plt.hist(iris["sepal_length"])
# sns.histplot(iris["sepal_length"],kde=True)
# selectNumeric = tips.select_dtypes(include="number")
# print("the numeric columns ",selectNumeric.columns)
# corRelation = selectNumeric.corr()
# print(corRelation.columns)
# sns.heatmap(corRelation, annot=True, cmap="viridis")
# plt.show()
tips = sns.load_dataset("tips")
# sns.set_style("dark")
# sns.set_palette("deep")
# sns.boxplot(x="day", y="total_bill", data=tips)


# sns.set_context("notebook")#other options are paper, talk, poster tell the size of the dot 
# sns.set_style("darkgrid")
# sns.set_palette("deep")
# sns.pairplot(tips)#hue is for highlights the data depends on the day 

print(tips.columns)
# sns.violinplot(x ="tip", y = "total_bill", data = tips ,hue="time", palette="muted")
sns.swarmplot(x="day", y="total_bill", data=tips, palette="muted")
plt.show()


