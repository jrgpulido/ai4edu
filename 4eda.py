#
#
#

# plot for min of each feature for each label class
iris.groupby(by = "class").min().plot(kind="bar")
#
iris.groupby(by = "class").max().plot(kind="bar")
#
iris.groupby(by = "class").mean().plot(kind="bar")

#
plt.figure()
class_series = iris.groupby('class').size()
class_series.name = ''#ribution
class_series.plot.pie(autopct='%.2f')
#plt.show()
