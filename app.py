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
    ngo = mongo.db.ngodata.find({"name":{'$regex': re.compile(r'\b{}\b'.format(ngoname),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    obj = [x for x in ngo]
    return toJson(obj)


@app.route('/regno/<regnum>')
def regno(regnum):
    ngo = mongo.db.ngodata.find({"regno":{"$regex": regnum}},{'_id': False})
    obj = [x for x in ngo]
    return toJson(obj)



@app.route('/city/<cityname>')
def city(cityname):
    ngo = mongo.db.ngodata.find({"city":{"$regex": re.compile(r'\b{}\b'.format(cityname),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    obj = [x for x in ngo]
    return toJson(obj)


@app.route('/state/<statename>')
def state(statename):
    ngo = mongo.db.ngodata.find({"state":{"$regex": re.compile(r'\b{}\b'.format(statename),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    obj = [x for x in ngo]
    return toJson(obj)


@app.route('/sector/<sectorname>')
def sector(sectorname):
    #ngo = mongo.db.ngodata.find({"sectors":{"$regex": sectorname,"$options": "-i"}})
    ngo = mongo.db.ngodata.find({'sectors':{'$regex': re.compile(r'\b{}\b'.format(sectorname),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    obj = [x for x in ngo]
    return toJson(obj)

if __name__ == '__main__':
    app.run(debug=True)
