#!/bin/python3
from math import e
from posixpath import basename
import joblib, os, sys, pandas as pd

#nifi
#indirme sudo apt-get install python3-pandas

######
#jfile = pd.read_json(sys.stdin, lines=True)

#Insert data
def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path,basename) for basename in files]
    return max(paths, key=os.path.getctime)


rf2 = joblib.load('/home/farplas/Desktop/Injection-machine-parameter-optimization/model/model_2021-04-21.joblib')
scaler = joblib.load("/home/farplas/Desktop/Injection-machine-parameter-optimization/scaler/scaler_2021-04-21.joblib")

#drop_list = ['cntCycle','stsMachine','timestamp','decMold']
#jfile = jfile.drop(drop_list, axis=1)
jfile = [(3276.7, 47.92, 51.4, 214.9, 45.8, 229.9, 214.9, 54.5, 55.3, 209.9, 72.67, 53.3, 220.0, 34.6, 295.2, 160.6, 77.0, 3276.7, 84.0, 3276.7, 3276.7, 39.6, 215.0, 3276.7, 3276.7, 3276.7, 39.27, 3276.7, 123.13, 3276.7, 3276.7, 3276.7, 2.69, 1.9, 0.124, 0.11, 7.0, 190.0, 3276.7, 210.4, 3276.7, 3276.7, 83.6, 3276.7, 29.3, 230.1, 43.9, 225.2, 3276.7, 235.2, 420.47, 427.507, 175.44, 180.485, 1.9, 2.69, 7.32, 3276.7, 3276.7, 3276.7, 3276.7, 1921.1, 54.4, 1382.0, 211.7, 1923.0, 1393.7, 1474.1, 1926.7, 79.74, 4201.8, 23.96, 23.69)]

data = scaler.transform(jfile)
prediction = pd.DataFrame(data)
result = rf2.predict_proba(prediction)
print(result)

#file1 = open('/home/farplas/Desktop/RF/result_test.txt', 'a')
#file1.write('\n'+str(jfile)+"----"+str(result))
#file1.close()

