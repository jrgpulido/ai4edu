#
#
#

#uni-
plt.title("uni-", fontsize=16)
iris.plot()

#bi-
iris.plot(kind="scatter", x="sepal width", y="sepal length")
plt.title("bi-", fontsize=16)
#vs
iris.plot(kind="scatter", x="sepal width", y="sepal width")
#vs
iris.plot(kind="scatter", x="sepal width", y="sepal length")

#
plt.figure()
plt.title("sepal width", fontsize=16)
iris["sepal width"].hist()
iris["sepal width"].value_counts()

#
plt.figure()
iris.boxplot()     
