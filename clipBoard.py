# plt.plot(air["station_london"], air["station_paris"],"r--")

# plt.hist(air["station_london"],density=True, facecolor="g", histtype='bar' ,bins=10)

# plt.bar(groups, values)
# plt.subplot(133)
# plt.hist(values, histtype='stepfilled', bins=1)

# fig, axes = plt.subplots(2,2, figsize=(10, 8))
# fig.suptitle("Subplots Example", fontsize=16)
# axes[0,0].scatter(groups,values)


# coolwarm
# viridis
# magma
# YlOrRd
# RdBu
# Blues
# Greens
# sns.heatmap(data, annot=True,cmap="RdBu")
import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
print(tips.columns)
# sns.boxplot(x="day", y="total_bill", data=tips)
print(iris.columns)
# sns.pairplot(iris, hue="sepal_width")
# sns.pairplot(iris)


sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
sns.histplot(iris["sepal_length"],kde=True)#kde for line 
print("the numeric columns ",selectNumeric.columns)
# corRelation = selectNumeric.corr()
# print(corRelation.columns)
# sns.heatmap(corRelation, annot=True, cmap="viridis")




# Seaborn Styles (sns.set_style()):
# "darkgrid" (default)
# "whitegrid"
# "dark"
# "white"
# "ticks"
# sns.set_style("dark")


# Seaborn Color Palettes (sns.set_palette()):
# Qualitative palettes:
# "deep"
# "muted"
# "pastel"
# "bright"
# "dark"
# "colorblind"
# sns.set_palette("deep")