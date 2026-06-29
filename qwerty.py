from sklearn.datasets import fetch_covtype
from sklearn.model_selection import train_test_split

covtype = fetch_covtype()
X, y = covtype.data, covtype.target
print(X)

