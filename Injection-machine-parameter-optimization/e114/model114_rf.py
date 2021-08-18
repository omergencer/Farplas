#!/bin/python3
import numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt, warnings, os.path, pickle
from sklearn import preprocessing
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
from imblearn.over_sampling import RandomOverSampler
from datetime import date
import joblib
warnings.filterwarnings("ignore")

### data import

df = pd.read_csv("/home/farplas/Desktop/Injection-machine-parameter-optimization/e114/360_inj_cyc_e114_deneme.csv")

## Convert reason(injection defect) data to 0(OK) and 1 (NOK)
df['reason'] = df['reason'].replace(['[]'],0)
df['reason'][df['reason'] != 0] = 1
df = df.astype({"reason": int})

#drop_list = ['Unnamed: 0', 'date', 'cntCycle','stsMachine','timestamp','sfc','decMold','prsInjectionHyd1','prsTransferHyd1','strCushion1','strPlasticisation1','strTransfer1']
#df = df.drop(drop_list, axis=1)
df = df.fillna(df.mean())

y = df['reason']
#X = df.drop(['reason'], axis=1)
X = df[['volCushion2', 'prsBackSpec2', 'timTransfer2', 'timTransfer1', 'volShot2', 'volPlasticisation1', 'timFill2' , 'timMoldOpen', 'tmpNozle2', 'prsTransferSpec2', 'prsInjectionSpec1', 'timPlasticisation2']]
Xx = df[['volCushion2', 'prsBackSpec2', 'timTransfer2', 'timTransfer1', 'volShot2', 'volPlasticisation1', 'timFill2' , 'timMoldOpen', 'tmpNozle2', 'prsTransferSpec2', 'prsInjectionSpec1', 'timPlasticisation2', 'reason']]


Xx.to_csv("out.csv", sep=',') 
'''
#Oversampling
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled = ros.fit_resample(X, y)
X = X_resampled
y = y_resampled

#Scale
scaler = preprocessing.StandardScaler().fit(X)
X = scaler.transform(X)
X = pd.DataFrame(X)
joblib.dump(scaler, "./e114/scaler/Standard_scaler_"+str(date.today())+".joblib")

#Train
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

#Random Forest
rf2=RandomForestClassifier(n_estimators=100, criterion='entropy',random_state=3)
model = rf2.fit(X_train,y_train)

#save model
joblib.dump(model,"./e114/model/Standard_model_"+str(date.today())+".joblib")

#Min Max

#Scale
scaler = preprocessing.MinMaxScaler().fit(X)
X = scaler.transform(X)
X = pd.DataFrame(X)
joblib.dump(scaler, "./e114/scaler/MM_scaler_"+str(date.today())+".joblib")

#Train
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

#Random Forest
rf2=RandomForestClassifier(n_estimators=100, criterion='entropy',random_state=3)
model = rf2.fit(X_train,y_train)

#save model
joblib.dump(model,"./e114/model/MM_model_"+str(date.today())+".joblib")
'''