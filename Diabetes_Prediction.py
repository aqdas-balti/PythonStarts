#Importing the Dependencies:
import NumPy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#Data Collection and Analysis
#PIMA Diabetes Dataset

#loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('\PythonStarts\diabetes.csv')
# pd.read_csv()