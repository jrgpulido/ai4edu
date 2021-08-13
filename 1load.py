#
# 
#

import pandas as pd
iris = pd.read_csv('iris+headers.csv')
#vs
#irisUn = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/bezdekIris.data')


#
iris.info()
#
type(iris)

#
iris.keys()
#
iris
