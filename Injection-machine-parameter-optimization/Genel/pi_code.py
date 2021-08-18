import pymysql, joblib, pandas as pd, RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)
io.setup(power_pin, io.OUT)

def blink(t):
    io.output(power_pin, io.LOW)
    sleep(t)
    io.output(power_pin, io.HIGH)
    sleep(t)

def connect():
    db = pymysql.connect(host = "192.168.7.17", port = 3306, db = "kepware", user = "nifiuser", passwd = "nHuSx6Y!")
    cursor = db.cursor()
    cursor.execute("SELECT tmpMoldZone25, timCool1, tmpBarrel2Zone3, tmpMoldZone3, tmpBarrel2Zone4, tmpFlange1, tmpMoldZone4, tmpBarrel2Zone1, tmpFlange2, tmpMoldZone1, volCushion1, tmpBarrel2Zone2, tmpMoldZone2, volCushion2, prsBackSpec2, prsBackSpec1, spdInjection1, tmpMoldZone9, spdInjection2, tmpMoldZone7, tmpMoldZone8, tmpOil, tmpMoldZone5, tmpMoldZone6, tmpMoldZone19, tmpMoldZone18, volTransfer2, tmpMoldZone15, volTransfer1, tmpMoldZone14, tmpMoldZone17, tmpMoldZone16, timTransfer2, timTransfer1, velPlasticisation2, velPlasticisation1, timMoldClose, tmpBarrel1Zone5, tmpMoldZone22, tmpBarrel1Zone4, tmpMoldZone21, tmpMoldZone24, tmpBarrel1Zone6, tmpMoldZone23, prsPomp1, tmpBarrel1Zone1, prsPomp2, tmpBarrel1Zone3, tmpMoldZone20, tmpBarrel1Zone2, volShot1, volPlasticisation2, volShot2, volPlasticisation1, timFill1, timFill2, timMoldOpen, tmpMoldZone11, tmpMoldZone10, tmpMoldZone13, tmpMoldZone12, prsHoldSpec2, tmpNozle2, prsHoldSpec1, tmpNozle1, prsTransferSpec2, prsTransferSpec1, prsInjectionSpec1, prsInjectionSpec2, timCycle, frcClamp, timPlasticisation1, timPlasticisation2 FROM e114 ORDER BY timestamp DESC LIMIT 1")
    val = cursor.fetchall()
    db.close()
    return val

def newest(path):
    files = os.listdir(path)
    paths = [os.path.join(path,basename) for basename in files]
    return max(paths, key=os.path.getctime)

def transform(data):
    data = pd.DataFrame(data)
    data = scaler.transform(data)
    return rf2.predict_proba(data)

try:
    rf2 = joblib.load(newest('/home/farplas/Desktop/RF/model'))#yoksa yap
    scaler = joblib.load(newest("/home/farplas/Desktop/RF/scaler"))
except FileNotFoundError:
    pass

power_pin = 27
old_val = None

while True:
    val = connect()
    if val != old_val:
        old_val = val
        res = transform(val)
        if res[0][1] > 0.1:
            blink(5)
