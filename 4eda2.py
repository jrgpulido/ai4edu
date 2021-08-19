#
#
#

#multi-
from pandas.plotting import scatter_matrix
scatter_matrix(iris)
#vs
scatter_matrix(iris,diagonal = 'kde')

#
plt.savefig('multi-variate.png')
