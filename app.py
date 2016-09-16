from flask import Flask
from flask.ext.pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'test'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

mongo = PyMongo(app)

@app.route('/ngoname/<ngoname>')
def ngoname(ngoname):
    ngo = mongo.db.ngodata.find_one({"name":{"$regex": ngoname}})
    return dumps(ngo)


@app.route('/regno/<regnum>')
def regno(regnum):
    ngo = mongo.db.ngodata.find_one({"regno":{"$regex": regnum}})
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
