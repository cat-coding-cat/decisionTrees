# Ejemplo implementamos un arbol de decisión para el dataset iris

import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import cross_val_score

# cargamos los datos
iris = load_iris()
X, y = iris.data,  iris.target

print(X[0])
print(y[0])
print(y[1])
#   hacemos un fit del clasicador
clf = DecisionTreeClassifier(splitter='random').fit(iris.data, iris.target)

# Los parámetros del DecisionTreeClassifier son
# class sklearn.tree.DecisionTreeClassifier(*, criterion='gini', splitter='best', max_depth=None, 
#                                              min_samples_split=2, min_samples_leaf=1, 
#                                              min_weight_fraction_leaf=0.0, max_features=None, 
#                                              random_state=None, max_leaf_nodes=None, 
#                                              min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0)


# cross validation
cv = cross_val_score(clf, iris.data, iris.target, cv=10)
print(cv)
# imprimimos el promedio de las 10 veces
print(sum(cv)/10)

# visualizamos el arbol
plot_tree(clf, filled=True)
plt.title("Decision tree trained using all the iris features")
plt.show()
