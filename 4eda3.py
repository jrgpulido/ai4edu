#
#
#

#
iris.plot.hist()
#
iris.plot.density()
#vs
iris.hist()



# create correlation matrix
corr = iris.corr()
print(corr)

#
import statsmodels.api as sm
sm.graphics.plot_corr(corr, xnames=list(corr.columns))


#class
plt.figure()
plt.scatter(x=iris['sepal width'], y=iris["sepal length"],
                c=iris[iris.columns[4]].astype('category').cat.codes,
                s=30, cmap=plt.cm.rainbow)
