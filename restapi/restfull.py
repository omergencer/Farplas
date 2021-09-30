from os import remove
from re import T
from flask import Flask, request, jsonify
from flask_sqlalchemy import  SQLAlchemy
from flask_marshmallow import Marshmallow
import json
import mysql.connector
from mysql.connector.cursor import RE_PY_MAPPING_PARAM
from pandas.io.json import json_normalize
from flask_restful import Api, Resource, marshal_with

app = Flask(__name__)
api = Api(app)

class datas(Resource):
    old_val = None
    def connect():
        db = mysql.connector.connect(host = "192.168.7.17", port = 3306, db = "kepware", user = "nifiuser", passwd = "nHuSx6Y!")
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM e117 ORDER BY timestamp DESC LIMIT 1")
        out = cursor.fetchall()
        db.close()
        return out



    def get(self):
        old_val = None
        val = datas.connect()
        if val != old_val:
            old_val = val
        #return jsonify(val[0])
        json_format = json.dumps(val[0], default=str)
        #json_format = jsonify(val[0])
        return json_format
    def post(self):
        old_val = None
        val = datas.connect()
        if val != old_val:
            old_val = val
        return jsonify(val[0])

api.add_resource(datas, "/data")
if __name__ == '__main__':
    app.run(port=5555,debug=True)