# https://scikit-learn.org/stable/tutorial/index.html
from sklearn import datasets
from sklearn.svm import SVC

#  the iris and digits datasets for classification and the diabetes dataset for regression.
iris = datasets.load_iris()
digits = datasets.load_digits()
diabetes = datasets.load_diabetes()

clf = SVC()
#clf.fit(iris.data, iris.target)
prediction = list(clf.predict(iris.data[:3]))
print(prediction)