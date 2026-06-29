import pandas as pd 
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_lw, y = load_wine(return_X_y = True)
X = StandardScaler()
print(X)


