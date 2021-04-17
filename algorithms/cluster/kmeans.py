from processdata import *
from sklearn import metrics

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

from sklearn.cluster import KMeans
import numpy as np
from math import *

num_cls = 4
kmc = KMeans(n_clusters=num_cls)
kmc.fit(x_train)

clusters = kmc.labels_

total = len(x_train)

xs_train = [[],[],[],[]]
ys_train = [[],[],[],[]]

cluster_size = [0] * num_cls
for i in range (total):
	cluster_size[clusters[i]] +=1
	xs_train[clusters[i]].append(x_train[i])
	ys_train[clusters[i]].append(y_train[i])

print("Centers of the clusters: ")
print(kmc.cluster_centers_)
print("Size of each clusters: ")
print(cluster_size)

print('\n')

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import tree

#create the knn model
#knn1 = KNeighborsClassifier(n_neighbors=int(sqrt(cluster_size[0])))
knn1 = tree.DecisionTreeClassifier()
#fit each model according to the training subsets
knn1.fit(xs_train[0], ys_train[0])

cl = kmc.predict(x_eval)

y0_eval = []
y_pred = []
for i in range(len(x_eval)):
	cl = kmc.predict([x_eval[i]])
	if cl[0] == 0:
		y0_eval.append(y_eval[i])
		yi = knn1.predict([x_eval[i]])
		y_pred.append(yi)

print("Decision Tree: Accuracy for evaluation set (cluster 0):",metrics.accuracy_score(y0_eval, y_pred))


knn2 = tree.DecisionTreeClassifier()
#fit each model according to the training subsets
knn2.fit(xs_train[1], ys_train[1])

cl = kmc.predict(x_eval)

y1_eval = []
y_pred = []
for i in range(len(x_eval)):
	cl = kmc.predict([x_eval[i]])
	if cl[0] == 1:
		y1_eval.append(y_eval[i])
		yi = knn1.predict([x_eval[i]])
		y_pred.append(yi)

print("Decision Tree: Accuracy for evaluation set (cluster 1):",metrics.accuracy_score(y1_eval, y_pred))
##############
knn3 = tree.DecisionTreeClassifier()
#fit each model according to the training subsets
knn3.fit(xs_train[2], ys_train[2])

cl = kmc.predict(x_eval)

y2_eval = []
y_pred = []
for i in range(len(x_eval)):
	cl = kmc.predict([x_eval[i]])
	if cl[0] == 2:
		y2_eval.append(y_eval[i])
		yi = knn1.predict([x_eval[i]])
		y_pred.append(yi)

print("Decision Tree: Accuracy for evaluation set (cluster 2):",metrics.accuracy_score(y2_eval, y_pred))
#################
knn4 = tree.DecisionTreeClassifier()
#fit each model according to the training subsets
knn4.fit(xs_train[3], ys_train[3])

cl = kmc.predict(x_eval)

y3_eval = []
y_pred = []
for i in range(len(x_eval)):
	cl = kmc.predict([x_eval[i]])
	if cl[0] == 3:
		y3_eval.append(y_eval[i])
		yi = knn1.predict([x_eval[i]])
		y_pred.append(yi)

print("Decision Tree: Accuracy for evaluation set (cluster 3):",metrics.accuracy_score(y3_eval, y_pred))
