from processdata import *

# get the training set
a = process_train_depression()
x_train = a[0]
y_train = a[1]

# get the evaluation set
a = process_eval_depression()
x_eval = a[0]
y_eval = a[1]

# get the test set
a = process_test_depression()
x_test = a[0]
y_test = a[1]

import numpy as np
from sklearn.gaussian_process import GaussianProcessClassifier

gp = GaussianProcessClassifier()
gp.fit(x_train, y_train)
y_pred = gp.predict(x_eval)
y_pred2 = gp.predict(x_test)

print(gp.score(x_train, y_train))

from sklearn import metrics
print("Precision for evaluation set:",metrics.precision_score(y_eval, y_pred))
print("Precision for test set:",metrics.precision_score(y_test, y_pred2))

print("recall for evaluation set:",metrics.recall_score(y_eval, y_pred))
print("recall for test set:",metrics.recall_score(y_test, y_pred2))

