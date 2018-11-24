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
import mycriteria

train_dataset = pd.read_csv("crime_train_preprocessed.csv")
X = train_dataset.drop(columns=['Category'])
y = train_dataset['Category']

rf = RandomForestClassifier(n_estimators=150, criterion="entropy", min_impurity_decrease=0.0002)
"""
n=50,  min=0.0002 -> 2.497
n=100, min=0.0002 -> 2.495
n=150, min=0.0002 -> 2.494
n=200, min=0.0002 -> 2.497
n=100, min=0.001 -> 2.555
n=300, min=0.001 -> 2.556
n=600, min=0.001 -> 2.556
"""
rskf = RepeatedStratifiedKFold(n_splits=3, n_repeats=1)
for train_index, test_index in rskf.split(X, y):
	rf = rf.fit(X.loc[train_index], y.loc[train_index])
	loss = log_loss(pd.get_dummies(y.loc[test_index]), rf.predict_proba(X.loc[test_index]))
	print loss

