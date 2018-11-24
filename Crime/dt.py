from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six.moves import zip
from sklearn.metrics import log_loss
from sklearn import preprocessing
from sklearn.model_selection import RepeatedStratifiedKFold
import random
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

train_dataset = pd.read_csv("crime_train_preprocessed.csv")
X = train_dataset.drop(columns=['Category'])
y = train_dataset['Category']
"""
bdt = AdaBoostClassifier(tree.DecisionTreeClassifier(splitter="random", max_depth=1), n_estimators=300, learning_rate=0.5)
rskf = RepeatedStratifiedKFold(n_splits=3, n_repeats=1)
for train_index, test_index in rskf.split(X, y):
	print "Fitting started..."
	bdt = bdt.fit(X.loc[train_index], y.loc[train_index])
	loss = log_loss(pd.get_dummies(y.loc[test_index]), bdt.predict_proba(X.loc[test_index]))
	print loss
"""
clf = tree.DecisionTreeClassifier(criterion="entropy", min_impurity_decrease=0.0002)# min_impurity_decrease=0.01)

rskf = RepeatedStratifiedKFold(n_splits=3, n_repeats=1)
for train_index, test_index in rskf.split(X, y):
	clf = clf.fit(X.loc[train_index], y.loc[train_index])
	loss = log_loss(pd.get_dummies(y.loc[test_index]), clf.predict_proba(X.loc[test_index]))
	print loss

