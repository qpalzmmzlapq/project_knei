import pandas as pd 
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

X, y = load_wine(return_X_y = True, as_frame = True)
print(X)
print(y)

