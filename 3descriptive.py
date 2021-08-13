#
#
#

#headers
iris.columns

iris["petal width"].value_counts()

iris["petal width"].value_counts().shape

iris["petal width"].mean()

iris.describe()
#vs
iris.sum()
iris.mean()
iris.min()
iris.max()

iris.head()
#
iris["petal width"].cumsum().head()
#
iris["petal width"].diff().head()
