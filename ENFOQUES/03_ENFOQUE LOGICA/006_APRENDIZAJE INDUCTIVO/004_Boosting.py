from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification

# Generar datos artificiales
X, y = make_classification(n_samples=100, n_features=5, random_state=42)

# Clasificador base
base_clf = DecisionTreeClassifier(max_depth=1)

# Aplicar boosting
boost_clf = AdaBoostClassifier(base_estimator=base_clf, n_estimators=50)
boost_clf.fit(X, y)

print("Precisión del modelo:", boost_clf.score(X, y))
