#
#
#

# mean for column by species
iris.groupby(by = "class").mean()

#
iris.groupby(by = "sepal width").mean()

#
iris.groupby(by = iris.columns[2]).mean()
