import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('oversight/salarypred/model/Engineering_graduate_salary.csv')
columns = ['ComputerProgramming','ElectronicsAndSemicon','ComputerScience','MechanicalEngg','ElectricalEngg','TelecomEngg','CivilEngg']
for col in columns:
    data[col] = data[col].replace({ -1 : np.nan})
    data[col] = data[col].fillna(data[col].mean())

def preprocess_inputs(df):
    df = df.copy()
     
    df = df.drop(['ID','CollegeID','CollegeCityID','10board','12board','CollegeState','DOB', '12graduation','GraduationYear','10percentage','12percentage'],axis=1)    
    
    df['Gender'] = df['Gender'].replace({'m': 0, 'f': 1}) 
    
    
    df['Degree'] = LabelEncoder().fit_transform(df.Degree)
    df['Specialization'] = LabelEncoder().fit_transform(df.Specialization)
        
    y = df['Salary']
    X = df.drop('Salary',axis=1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=43)
    
    scaler = StandardScaler()
    scaler.fit(X_train)
    
    X_train = pd.DataFrame(scaler.transform(X_train), columns = X_train.columns, index = X_train.index)
    X_test = pd.DataFrame(scaler.transform(X_test), columns = X_test.columns, index = X_test.index)
    
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = preprocess_inputs(data)

model = LinearRegression().fit(X_train, y_train)
