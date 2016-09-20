from flask import Flask,render_template,jsonify
from flask.ext.pymongo import PyMongo
from bson import json_util
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
    ngo = mongo.db.ngodata.find({"name":{"$regex": ngoname}})
    obj = [x for x in ngo]
    return toJson(obj)
    # for i in range(len(obj)):
    #     obj[i].pop('_id')
    # return jsonify(obj)


@app.route('/regno/<regnum>')
def regno(regnum):
    ngo = mongo.db.ngodata.find({"regno":{"$regex": regnum}})
    return dumps(ngo)



@app.route('/city/<cityname>')
def city(cityname):
    ngo = mongo.db.ngodata.find({"city":{"$regex": cityname}})
    return dumps(ngo)


@app.route('/state/<statename>')
def state(statename):
    ngo = mongo.db.ngodata.find({"state":{"$regex": statename}})
    return dumps(ngo)


@app.route('/sector/<sectorname>')
def sector(sectorname):
    ngo = mongo.db.ngodata.find({"sectors":{"$regex": sectorname}})
    return dumps(ngo)

if __name__ == '__main__':
    app.run(debug=True)
