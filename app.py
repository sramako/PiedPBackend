import os
from flask import Flask
from flask import request
import json
from flask_cors import CORS, cross_origin
import pymongo

app = Flask(__name__)

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

@app.route('/categorycontent')
def categorycontent():
	mycol = mydb["places"]
	name = request.args.get('name')
	category = request.args.get('category')
	m = []
	for i in mycol.find({'name':name},{'_id':0, 'Menu':1}):
		m.append(i['Menu'])
	m=m[0]
	menu=dict()
	for i in m:
		if i["name"]==category:
			for dish in i["items"]:
				menu[dish["name"]]=dish["price"]
	return json.dumps(menu, separators=(',',':'))

@app.route('/price')
def price():
	mycol = mydb["places"]
	name = request.args.get('restaurant')
	category = request.args.get('item')
	m = []
	for i in mycol.find({'name':name},{'_id':0, 'Menu':1}):
		m.append(i['Menu'])
	m=m[0]
	menu=dict()
	for i in m:
		for dish in i["items"]:
			if(dish["name"]==category):
				print(dish["price"])
				return json.dumps({"price":dish["price"]}, separators=(',',':'))

	return "{price:NF}"

@app.route('/category')
def category():
	mycol=mydb['places']
	name=request.args.get('name')
	m=[]
	for i in mycol.find({'name':name},{'_id':0, 'Menu':1}):
		m.append(i['Menu'])
	m=m[0]
	menu=[]
	# key="category"
	# menu["category"]={}
	# items=[]
	for i in m:
		menu.append(i['name'])
	return json.dumps(menu,separators=(',',':'))

@app.route('/payment')
	def category():
		mycol=mydb['payments']
		name=request.args.get('name')
		check=mycol.find_one({"user":name},{"_id":0})
		if(check==None):
			mycol.insert_one({"user":name,"status":0})
		check=mycol.find_one({"user":name},{"_id":0})
		if(check['status']==0):
			return json.dumps({"status":"waiting"},separators=(',',':'))
		elif(check['status']==1):
			mycol.delete_one({"user":"Sraman"})
			return json.dumps({"status":"success"},separators=(',',':'))

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	CORS(app, resources=r'/*')
	# app.config['CORS_HEADERS'] = 'Content-Type'
	app.run(host='0.0.0.0', port=port)
	# app.run()
