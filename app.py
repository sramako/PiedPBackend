import os
from flask import Flask
from flask import request
import json

app = Flask(__name__)

import pymongo
myclient = pymongo.MongoClient("mongodb://sraman:sraman123@ds157223.mlab.com:57223/webtech2proj")
mydb = myclient['webtech2proj']

@app.route('/')
def hello():
    return 'Ako: All endponts are live.'

@app.route('/menu')
def menu():
	mycol = mydb["places"]
	name = request.args.get('name')
	m = []
	for i in mycol.find({'name':name},{'_id':0, 'Menu':1}):
		m.append(i['Menu'])
	return json.dumps(m, separators=(',',':'))

@app.route('/restaurants')
def restaurants():
	mycol = mydb["places"]
	ret = []
	for i in mycol.find({},{'_id':0, 'name':1}):
		ret.append(i['name'])
	return ' '.join(ret)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
	port = int(os.environ.get('PORT', 5000))
	# app.run()
