from flask import Flask, request, jsonify
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import Marshmallow
import json
import mysql.connector
from pandas.io.json import json_normalize
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
    
def connect():
    """enj"""
    db = mysql.connector.connect(host = "192.168.7.17", port = 3306, db = "kepware", user = "nifiuser", passwd = "nHuSx6Y!")
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM e117 ORDER BY timestamp DESC LIMIT 1")
    #row_headers=[x[0] for x in cursor.description] #this will extract row headers
    out = cursor.fetchall()
    db.close()
    return out
    #return json.dumps(out,indent=4,sort_keys=True, default=str)


old_val = None

@app.route('/data', methods = ['GET'])
def get():
    old_val = None
    val = connect()
    if val != old_val:
        old_val = val
    return jsonify(val[0])

if __name__ == '__main__':
    app.run(port=5555,debug=True)