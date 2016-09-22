from flask import Flask,render_template,jsonify,request
from flask.ext.pymongo import PyMongo
from bson import json_util
import re
import json

app = Flask(__name__,static_url_path='')
app.config['MONGO_DBNAME'] = 'test'  #set mongo database name here 
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test' # set mongo connection string


mongo = PyMongo(app)

def splitdata(obj,limit):
    splitlist = [list(i) for i in zip(*[iter(obj)]*limit)]
    splitlist.append(obj[len(splitlist)*limit:])
    return splitlist



def toJson(data):
    return json.dumps(data, default=json_util.default)



@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/ngoname/<ngoname>')
def ngoname(ngoname):
    ngo = mongo.db.ngodata.find({"name":{'$regex': re.compile(r'\b{}\b'.format(ngoname),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    page = request.args.get('page')
    limit = request.args.get('limit')
    obj = [x for x in ngo]
    if page is None or limit is None:
        return toJson(obj)
    else:
        res = splitdata(obj,int(limit))
        for i in range(len(res)):
            res[i] = [{"_metadata":{"page":page,"page_count":str(len(res)),"limit":limit}}] + res[i]
        try:
            return toJson(res[int(page)-1])
        except IndexError:
            return toJson([])


@app.route('/regno/<regnum>')
def regno(regnum):
    ngo = mongo.db.ngodata.find({"regno":{"$regex": regnum}},{'_id': False})
    page = request.args.get('page')
    limit = request.args.get('limit')
    obj = [x for x in ngo]
    if page is None or limit is None:
        return toJson(obj)
    else:
        res = splitdata(obj,int(limit))
        for i in range(len(res)):
            res[i] = [{"_metadata":{"page":page,"page_count":str(len(res)),"limit":limit}}] + res[i]
        try:
            return toJson(res[int(page)-1])
        except IndexError:
            return toJson([])



@app.route('/city/<cityname>')
def city(cityname):
    ngo = mongo.db.ngodata.find({"city":{"$regex": re.compile(r'\b{}\b'.format(cityname),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    page = request.args.get('page')
    limit = request.args.get('limit')
    obj = [x for x in ngo]
    if page is None or limit is None:
        return toJson(obj)
    else:
        res = splitdata(obj,int(limit))
        for i in range(len(res)):
            res[i] = [{"_metadata":{"page":page,"page_count":str(len(res)),"limit":limit}}] + res[i]
        try:
            return toJson(res[int(page)-1])
        except IndexError:
            return toJson([])



@app.route('/state/<statename>')
def state(statename):
    ngo = mongo.db.ngodata.find({"state":{"$regex": re.compile(r'\b{}\b'.format(statename),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    page = request.args.get('page')
    limit = request.args.get('limit')
    obj = [x for x in ngo]
    if page is None or limit is None:
        return toJson(obj)
    else:
        res = splitdata(obj,int(limit))
        for i in range(len(res)):
            res[i] = [{"_metadata":{"page":page,"page_count":str(len(res)),"limit":limit}}] + res[i]
        try:
            return toJson(res[int(page)-1])
        except IndexError:
            return toJson([])


@app.route('/sector/<sectorname>')
def sector(sectorname):
    ngo = mongo.db.ngodata.find({'sectors':{'$regex': re.compile(r'\b{}\b'.format(sectorname),re.IGNORECASE) ,"$options": "-i"}},{'_id': False})
    page = request.args.get('page')
    limit = request.args.get('limit')
    obj = [x for x in ngo]
    if page is None or limit is None:
        return toJson(obj)
    else:
        res = splitdata(obj,int(limit))
        for i in range(len(res)):
            res[i] = [{"_metadata":{"page":page,"page_count":str(len(res)),"limit":limit}}] + res[i]
        try:
            return toJson(res[int(page)-1])
        except IndexError:
            return toJson([])



if __name__ == '__main__':
    app.run(debug=True)
