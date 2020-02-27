# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Load the data
df = pd.read_csv(path)

# replace the $ symbol
columns = ['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']

for col in columns:
    df[col].replace({'\$': '', ',': ''}, regex=True,inplace=True)

# store independent variable
X = df.drop(['CLAIM_FLAG'],axis=1)

# store dependent variable
y = df['CLAIM_FLAG']

# Check the value counts
count = y.value_counts()
print(count)

# spliting the dataset
X_train,X_test,y_train,y_test=train_test_split(X,y ,test_size=0.3,random_state=6)




# --------------
# Code starts here
columns=['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']
X_train=X_train[columns].astype(float)
X_test=X_test[columns].astype(float)
X_train.isna().sum()
X_test.isna().sum()
# Code ends here


# --------------
# Code starts here
X_train[['YOJ','OCCUPATION']]=X_train.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
X_test[['YOJ','OCCUPATION']]=X_test.dropna(subset=['YOJ','OCCUPATION'],inplace=True)

#X_test[['YOJ','OCCUPATION']].isna().sum()
y_train=y_train[X_train.index]
y_test=y_test[X_test.index]

X_train[['AGE','CAR_AGE','INCOME','HOME_VAL']]=X_train[['AGE','CAR_AGE','INCOME','HOME_VAL']].fillna(X_train.mean(),inplace=True)
X_test[['AGE','CAR_AGE','INCOME','HOME_VAL']]=X_test[['AGE','CAR_AGE','INCOME','HOME_VAL']].fillna(X_test.mean(),inplace=True)
#print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)
# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
for col in columns:
    le=LabelEncoder()
    X_train[col]=le.fit_transform(X_train[col].astype(str))
    X_test[col]=le.fit_transform(X_test[col].astype(str))


# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression



# code starts here 
model=LogisticRegression(random_state = 6)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
score=accuracy_score(y_test,y_pred)
print('accuracy score is')


# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
smote=SMOTE(random_state = 9)
X_train,y_train=smote.fit_sample(X_train,y_train)
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# Code ends here


# --------------
# Code Starts here
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
score=accuracy_score(y_test,y_pred)
print(score)

# Code ends here


