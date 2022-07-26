# Ejemplo implementamos un arbol de decisión para el dataset iris

import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import cross_val_score
import pandas as pd

# cargamos los datos
df = pd.read_csv('./drug200.csv')


from sklearn.model_selection import train_test_split

x_train,x_test, y_train, y_test = train_test_split(df,df.Drug)

print(x_train)
print(y_train)
#   hacemos un fit del clasicador
clf = DecisionTreeClassifier(splitter='random').fit(x_train, y_train)

# Los parámetros del DecisionTreeClassifier son
# class sklearn.tree.DecisionTreeClassifier(*, criterion='gini', splitter='best', max_depth=None, 
#                                              min_samples_split=2, min_samples_leaf=1, 
#                                              min_weight_fraction_leaf=0.0, max_features=None, 
#                                              random_state=None, max_leaf_nodes=None, 
#                                              min_impurity_decrease=0.0, class_weight=None, ccp_alpha=0.0)


# score
model_score = clf.score(x_test, y_test)
print("model score", model_score)


cv = cross_val_score(clf, df, df.Drug, cv=10)
print(cv)

# visualizamos el arbol
plot_tree(clf, filled=True)
plt.title("Desing Drugs for patients")
plt.show()
