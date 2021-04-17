from processdata import *
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=40)

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

knn.fit(x_train, y_train)

y_pred = knn.predict(x_eval)
y_pred2 = knn.predict(x_test)

from sklearn import metrics
print("Accuracy for evaluation set (depression):",metrics.accuracy_score(y_eval, y_pred))
print("Accuracy for test set (depression):",metrics.accuracy_score(y_test, y_pred2))

knn1 = KNeighborsClassifier(n_neighbors=40)

# get the training set
a = process_train_anxiety()
x_train2 = a[0]
y_train2 = a[1]

# get the evaluation set
a = process_eval_anxiety()
x_eval2 = a[0]
y_eval2 = a[1]

# get the test set
a = process_test_anxiety()
x_test2 = a[0]
y_test2 = a[1]

knn1.fit(x_train2, y_train2)

y_pred3 = knn1.predict(x_eval2)
y_pred4 = knn1.predict(x_test2)

from sklearn import metrics
print("Accuracy for evaluation set (anxiety):",metrics.accuracy_score(y_eval2, y_pred3))
print("Accuracy for test set (anxiety):",metrics.accuracy_score(y_test2, y_pred4))