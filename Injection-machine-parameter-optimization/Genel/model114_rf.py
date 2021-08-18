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

df = pd.read_csv("360_inj_cyc_e114_deneme.csv")

## Convert reason(injection defect) data to 0(OK) and 1 (NOK)
df['reason'] = df['reason'].replace(['[]'],0)
df['reason'][df['reason'] != 0] = 1
df = df.astype({"reason": int})

drop_list = ['Unnamed: 0', 'date', 'cntCycle','stsMachine','timestamp','sfc','decMold','prsInjectionHyd1','prsTransferHyd1','strCushion1','strPlasticisation1','strTransfer1']
df = df.drop(drop_list, axis=1)
df = df.fillna(df.mean())

y = df['reason']
X = df.drop(['reason'], axis=1)

#Oversampling
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled = ros.fit_resample(X, y)


X = X_resampled
y = y_resampled

#Scale
#scaler = preprocessing.MinMaxScaler().fit(X)
#X = scaler.transform(X)
#X = pd.DataFrame(X)
#joblib.dump(scaler, "./scaler/scaler_"+str(date.today())+".joblib")


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

#Random Forest
rf2=RandomForestClassifier(n_estimators=100, criterion='entropy',random_state=3)
model = rf2.fit(X_train,y_train)
y_rf2=rf2.predict(X_val)
y_rf_prob2=rf2.predict_proba(X_val)[:,1]

#save model
#date =date.isoformat()

joblib.dump(rf2,"./model/model_"+str(date.today())+".joblib")
