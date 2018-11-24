import pymongo
myclient = pymongo.MongoClient("mongodb://sraman:sraman123@ds157223.mlab.com:57223/webtech2proj")
mydb = myclient['webtech2proj']

# print(mydb.list_collection_names())
mycol = mydb["places"]

mydict = { "name": "KFC", "address": "Kathriguppe" }

mydict = {
  "name": "KFC",
  "Menu": [
    {
      "name": "Chicken",
      "items": [
        {
          "name": "Big8",
          "price": "523.81"
        },
        {
          "name": "Big8Meal",
          "price": "647.62"
        },
        {
          "name": "HotandCrispy",
          "price": "195.24"
        },
        {
          "name": "FriendshipBucketMeal",
          "price": "657.14"
        },
        {
          "name": "TripleTreat",
          "price": "642.86"
        },
        {
          "name": "Click and Share",
          "price": "380.00"
        },
        {
          "name": "FrienshipBucket",
          "price": "614.29"
        },
        {
          "name": "MinglesBucket",
          "price": "284.76"
        },
        {
          "name": "SmokyGrilled4Pcs",
          "price": "361.90"
        },
        {
          "name": "SmokyGrilled6Pcs",
          "price": "361.90"
        },
        {
          "name": "SmokyGrilled8Pcs",
          "price": "361.90"
        }
      ]
    },
    {
      "name": "Burgers",
      "items": [
        {
          "name": "5in1ZingerBox",
          "price": "227.62"
        },
        {
          "name": "ChickenZinger",
          "price": "152.38"
        },
        {
          "name": "VegZinger",
          "price": "138.10"
        },
        {
          "name": "VegLonger",
          "price": "71.43"
        }
      ]
    },
    {
      "name": "Snacks",
      "items": [
        {
          "name": "LargePopcorn",
          "price": "190.48"
        },
        {
          "name": "VegStrips4Pcs",
          "price": "123.81"
        },
        {
          "name": "BonelessStrips6Pcs",
          "price": "204.76"
        },
        {
          "name": "LargePopcorn",
          "price": "190.48"
        },
        {
          "name": "HotWings4Pcs",
          "price": "128.57"
        },
        {
          "name": "SmokyGrilled1Pc",
          "price": "104.76"
        },
        {
          "name": "SmokyGrilled2Pcs",
          "price": "190.48"
        }
      ]
    },
    {
      "name": "RiceBowlz",
      "items": [
        {
          "name": "5in1RiceBox",
          "price": "227.62"
        },
        {
          "name": "CickenRiceBowl",
          "price": "142.86"
        }
      ]
    },
    {
      "name": "Beverages",
      "items": [
        {
          "name": "Pepsi",
          "price": "28.57"
        },
        {
          "name": "RedBull",
          "price": "138.10"
        }
      ]
    }
  ]
}

mycol.insert_one(mydict)

mycol.delete_one({'name':'KFC'})

//GET MENU
for i in mycol.find({'name':'KFC'},{'_id':0, 'Menu':1}):
	print(i['Menu'])

//GET restaurants
for i in mycol.find({},{'_id':0, 'name':1}):
	print(i['name'])


mycol = mydb["payments"]
mycol.delete_many({})

mycol.insert_one({"user":"Sraman","status":1})
mycol.delete_one({"user":"Sraman"})

check

check=mycol.find_one({"user":"Sraman"},{"_id":0})
if(check==None):
	mycol.insert_one({"user":"Sraman","status":0})
	check=mycol.find_one({"user":"Sraman"},{"_id":0})
if(check['status']==0):
	return 0
elif(check['status']==1):
	mycol.delete_one({"user":"Sraman"})
	mycol.insert_one({"user":"Sraman","status":0})
	return 1


mydict={"name": "KFC", "VegZinger": 4, "ChickenZinger": 2}

mydict
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

items = list(mydict.keys())
items

mycol=mydb["orders"]
for i in mycol.find():
	print(i)

freq = dict()
for i in mycol.find({'user':'Sraman'},{'_id':0,'items':1}):
	print(i['items'])
	l = i['items']
	items = list(l.keys())
	for item in items:
		if l[item] in freq:
			freq[l[item]].append(item)
		else:
			freq[l[item]]=[item]

freq[4].append("Hello")
freq

mycol.delete_one({'name': 'Taza Tindi'})

for i in mycol.find({'name': 'Taza Tindi'},{'menu':1}):
	print(i)

q = 'chicken'
mycol=mydb["places"]
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
















KFC
{'name': 'KFC', 'Menu': [{'name': 'Chicken', 'items': [{'name': 'Big8', 'price': '523.81'}, {'name': 'Big8Meal', 'price': '647.62'}, {'name': 'HotandCrispy', 'price': '195.24'}, {'name': 'FriendshipBucketMeal', 'price': '657.14'}, {'name': 'TripleTreat', 'price': '642.86'}, {'name': 'Click and Share', 'price': '380.00'}, {'name': 'FrienshipBucket', 'price': '614.29'}, {'name': 'MinglesBucket', 'price': '284.76'}, {'name': 'SmokyGrilled4Pcs', 'price': '361.90'}, {'name': 'SmokyGrilled6Pcs', 'price': '361.90'}, {'name': 'SmokyGrilled8Pcs', 'price': '361.90'}]}, {'name': 'Burgers', 'items': [{'name': '5in1ZingerBox', 'price': '227.62'}, {'name': 'ChickenZinger', 'price': '152.38'}, {'name': 'VegZinger', 'price': '138.10'}, {'name': 'VegLonger', 'price': '71.43'}]}, {'name': 'Snacks', 'items': [{'name': 'LargePopcorn', 'price': '190.48'}, {'name': 'VegStrips4Pcs', 'price': '123.81'}, {'name': 'BonelessStrips6Pcs', 'price': '204.76'}, {'name': 'LargePopcorn', 'price': '190.48'}, {'name': 'HotWings4Pcs', 'price': '128.57'}, {'name': 'SmokyGrilled1Pc', 'price': '104.76'}, {'name': 'SmokyGrilled2Pcs', 'price': '190.48'}]}, {'name': 'RiceBowlz', 'items': [{'name': '5in1RiceBox', 'price': '227.62'}, {'name': 'CickenRiceBowl', 'price': '142.86'}]}, {'name': 'Beverages', 'items': [{'name': 'Pepsi', 'price': '28.57'}, {'name': 'RedBull', 'price': '138.10'}]}]}
Taza Tindi
{'name': 'Taza Tindi', 'address': 'Katriguppe', 'menu': [{'name': 'South Indian', 'items': [{'name': 'idly', 'price': '15'}, {'name': 'vada', 'price': '14'}, {'name': 'Dosa', 'price': '40'}, {'name': 'coffee', 'price': '10'}, {'name': 'tea', 'price': '10'}, {'price': '20', 'name': 'badam milk'}]}, {'name': 'North Indian', 'items': [{'name': 'Roti', 'price': '10'}, {'name': 'Kulcha', 'price': '20'}, {'name': 'Naan', 'price': '20'}]}, {'name': 'Drinks', 'items': []}]}
Taza Tindi
{'name': 'Taza Tindi', 'address': 'Katriguppe', 'menu': [{'name': 'South Indian', 'items': [{'name': 'idly', 'price': '15'}, {'name': 'vada', 'price': '20'}, {'name': 'Dosa', 'price': '40'}, {'name': 'coffee', 'price': '10'}, {'name': 'tea', 'price': '10'}, {'price': '20', 'name': 'badam milk'}]}, {'name': 'North Indian', 'items': [{'name': 'Roti', 'price': '10'}, {'name': 'Kulcha', 'price': '20'}, {'name': 'Naan', 'price': '20'}]}, {'name': 'Drinks', 'items': []}]}
Jalsa
{'name': 'Jalsa', 'address': 'Katriguppe', 'Menu': [{'name': 'Veg', 'items': [{'name': 'Paneer', 'price': '150'}, {'name': 'Gobi', 'price': '200'}, {'name': 'Aloo', 'price': '120'}, {'name': 'Beer', 'price': '200'}, {'name': 'Vodka', 'price': '400'}, {'name': 'Soda', 'price': '20'}]}, {'name': 'Non-Veg', 'items': [{'name': 'Chicken', 'price': '200'}, {'name': 'Mutton', 'price': '250'}, {'name': 'Fish', 'price': '300'}]}, {'name': 'Drinks', 'items': []}]}
BBQ Nation
{'name': 'BBQ Nation', 'address': 'JP nagar', 'Menu': [{'name': 'Grills', 'items': [{'name': 'Chicken Kabab', 'price': '340'}, {'name': 'Paneer tikka', 'price': '290'}, {'name': 'Fish Tikka', 'price': '300'}]}, {'name': 'Drinks', 'items': [{'name': 'fresh lime soda', 'price': '120'}, {'name': 'coke', 'price': '90'}, {'name': 'lassi', 'price': '90'}]}, {'name': 'Main Course', 'items': [{'name': 'Paneer Kadai', 'price': '170'}, {'name': 'Naan', 'price': '60'}, {'name': 'Chicken Gravy', 'price': '210'}]}]}
Echoes
{'name': 'Echoes', 'address': 'Koramangala', 'Menu': [{'name': 'Apetizers', 'items': [{'name': 'tandoori momo', 'price': '190'}, {'name': 'alfredo veg', 'price': '140'}, {'name': 'kitkat milkshake', 'price': '120'}]}, {'name': 'Main Course', 'items': [{'name': 'Paneer A1', 'price': '150'}, {'name': 'Kerela Paratha', 'price': '60'}, {'name': 'Aloo Paratha', 'price': '80'}]}, {'name': 'Deserts', 'items': [{'name': 'Pineapple Cake', 'price': '110'}, {'name': 'Sundae', 'price': '200'}, {'name': 'Vanilla milkshake', 'price': '90'}]}]}
Taza Tindi
{'name': 'Taza Tindi', 'address': 'Katriguppe', 'Menu': [{'name': 'South Indian', 'items': [{'name': 'idly', 'price': '15'}, {'name': 'vada', 'price': '14'}, {'name': 'Dosa', 'price': '30'}]}, {'name': 'North Indian', 'items': [{'name': 'Roti', 'price': '10'}, {'name': 'Kulcha', 'price': '20'}, {'name': 'Naan', 'price': '20'}]}, {'name': 'Drinks', 'items': [{'name': 'coffee', 'price': '10'}, {'name': 'tea', 'price': '10'}, {'name': 'badam milk', 'price': '20'}]}]}
