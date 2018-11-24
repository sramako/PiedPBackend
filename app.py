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

@app.route('/delivery')
def delivery():
	mycol=mydb['places']
	name=request.args.get('user')
	m=dict()
	if(name=="Ako"):
		m = {"start":{"x":"12.93657","y":"77.579887"},"end":{"x":"12.935157","y":"77.53656"}}
	return json.dumps(m,separators=(',',':'))

@app.route('/userdata')
def userdata():
	mycol=mydb['orders']
	name=request.args.get('user')
	freq = dict()
	for i in mycol.find({'user':name},{'_id':0,'items':1}):
		print(i['items'])
		l = i['items']
		items = list(l.keys())
		for item in items:
			if l[item] in freq:
				freq[l[item]].append(item)
			else:
				freq[l[item]]=[item]
	return json.dumps(freq,separators=(',',':'))

@app.route('/payment')
def payment():
	mycol=mydb['payments']
	name=request.args.get('name')
	check=mycol.find_one({"user":name},{"_id":0})
	if(check==None):
		mycol.insert_one({"user":name,"status":0})
	check=mycol.find_one({"user":name},{"_id":0})
	if(check['status']==0):
		return json.dumps({"status":"waiting"},separators=(',',':'))
	elif(check['status']==1):
		mycol.delete_one({"user":name})
		return json.dumps({"status":"success"},separators=(',',':'))

@app.route('/paymentgateway')
def gateway():
	mycol=mydb['payments']
	name=request.args.get('name')
	check=mycol.find_one({"user":name},{"_id":0})
	if(check==None):
		return json.dumps({"status":"failed"},separators=(',',':'))
	elif(check['status']==0):
		mycol.delete_one({"user":name})
		mycol.insert_one({"user":name,"status":1})
		return json.dumps({"status":"success"},separators=(',',':'))
	elif(check['status']==1):
		return json.dumps({"status":"aborted"},separators=(',',':'))

@app.route('/addRestaurant', methods=['GET', 'POST'])
def add_Res():
    if request.method == 'POST':
        obj = request.get_json(force=True)
        mydb['places'].insert(obj)
        return 'Success'
    return 'not post'

@app.route('/order', methods=['GET', 'POST'])
def order():
	if request.method == 'POST':
		mydict = request.get_json(force=True)
		print(mydict)
		restaurant = mydict["name"]
		user = mydict["user"]
		lat = mydict["lat"]
		long = mydict["long"]
		del mydict['name']
		del mydict['user']
		del mydict['lat']
		del mydict['long']
		food = mydict
		order=dict()
		order["restaurant"] = restaurant
		order["user"] = user
		order["lat"] = lat
		order["long"] = long
		order["items"] = food
		print(order)
		mydb['orders'].insert(order)
		return 'Success'
	return 'not post'

@app.route('/search')
def search():
	mycol=mydb['payments']
	q=request.args.get('query')
	q=q.lower()
	mycol=mydb["places"]
	m = dict()
	for i in mycol.find({},{'_id':0}):
		name=i['name']
		for categories in i['Menu']:
			if q in categories['name'].lower():
				for dish in categories['items']:
					if name in m:
						m[name].append(dish['name'])
					else:
						m[name]=[dish['name']]

			else:
				for dish in categories['items']:
					if q in dish['name'].lower():
						if name in m:
							m[name].append(dish['name'])
						else:
							m[name]=[dish['name']]
		return json.dumps(m,separators=(',',':'))

# endpoint to handle login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        obj = request.get_json(force=True)
        users = mydb['users']
        login_user = users.find_one({'username' : obj['username']})
        if login_user:
            if obj['password']==login_user['password']:
                # Session['username'] = obj['username']
                return 'Success'
    return 'Failure'

# endpoint to handle Sign-up
@app.route('/signUp', methods=['GET','POST'])
def signUp():
    user = request.form['username']
    p1 = request.form['password1']
    p2 = request.form['password2']
    if p1==p2:
        mydb['users'].insert({"username":user,"password":p1})
        return 'Success'
    return 'Failure'

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	CORS(app, resources=r'/*')
    # app.config['CORS_HEADERS'] = 'Content-Type'
	app.run(host='0.0.0.0', port=port,debug=True)
	# app.run()
