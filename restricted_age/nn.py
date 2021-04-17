from sklearn.neural_network import MLPClassifier
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

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

clf.fit(x_train, y_train)
y_pred = clf.predict(x_eval)
y_pred2 = clf.predict(x_test)

from sklearn import metrics
print("Accuracy for evaluation set:",metrics.accuracy_score(y_eval, y_pred))
print("Accuracy for test set:",metrics.accuracy_score(y_test, y_pred2))

