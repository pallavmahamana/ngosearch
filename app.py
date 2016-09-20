from flask import Flask,render_template,jsonify
from flask.ext.pymongo import PyMongo
from bson import json_util
import re
import json

app = Flask(__name__,static_url_path='')
app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

def toJson(data):
    return json.dumps(data, default=json_util.default)



@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/ngoname/<ngoname>')
def ngoname(ngoname):
    ngo = mongo.db.ngodata.find({"name":{'$regex':ngoname ,"$options": "-i"}})
    obj = [x for x in ngo]
    return toJson(obj)


@app.route('/regno/<regnum>')
def regno(regnum):
    ngo = mongo.db.ngodata.find({"regno":{"$regex": regnum}})
    obj = [x for x in ngo]
    return toJson(obj)



@app.route('/city/<cityname>')
def city(cityname):
    ngo = mongo.db.ngodata.find({"city":{"$regex": cityname,"$options": "-i"}})
    obj = [x for x in ngo]
    return toJson(obj)


@app.route('/state/<statename>')
def state(statename):
    ngo = mongo.db.ngodata.find({"state":{"$regex": statename,"$options": "-i"}})
    obj = [x for x in ngo]
    return toJson(obj)


@app.route('/sector/<sectorname>')
def sector(sectorname):
    ngo = mongo.db.ngodata.find({"sectors":{"$regex": sectorname}})
    obj = [x for x in ngo]
    return toJson(obj)

if __name__ == '__main__':
    app.run(debug=True)
