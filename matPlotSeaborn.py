import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

air = pd.read_csv("air.csv")
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
plt.hist(iris.data[:,0])
plt.show()