import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv('oversight/salarypred/model/Engineering_graduate_salary.csv')

def preprocess_inputs(df):
    df = df.copy()
     
    df = df.drop(['ID','CollegeID','CollegeCityID','10board','12board','CollegeState','DOB', 'CollegeCityTier','12graduation','10percentage','12percentage'],axis=1)    
    
    df['Gender'] = df['Gender'].replace({'m': 0, 'f': 1}) 
    
    df['Degree'] = df['Degree'].replace({'B.Tech/B.E.': 0, 'M.Tech./M.E.': 1})
        
    df['Specialization'] = df['Degree'].replace({'computer science & engineering': 0, 'electronics & telecommunications': 1, 'information technology': 2,'automobile/automotive engineering': 3 , 'biotechnology': 4, 'mechanical engineering': 5,
                                                 'instrumentation engineering': 6, 'aeronautical engineering': 7, 'biomedical engineering': 8,'chemical engineering': 9 , 'civil engineering': 10, 'computer engineering': 11,
                                                 'electrical engineering': 12, 'telecommunication engineering': 13, 'industrial engineering': 14,'electronics and computer engineering': 15 , 'electronics engineering': 16, 'mechatronics': 17,
                                                 'other': 18})
        
    y = df['Salary']
    X = df.drop('Salary',axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=43)
    
    """scaler = StandardScaler()
    scaler.fit(X_train)
    
    X_train = pd.DataFrame(scaler.transform(X_train), columns = X_train.columns, index = X_train.index)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns, index = X_test.index)"""
    
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = preprocess_inputs(data)

model = LinearRegression().fit(X_train, y_train)

filename='salarypredmodel.sav'
joblib.dump(model,filename)