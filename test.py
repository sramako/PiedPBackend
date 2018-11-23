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



for i in mycol.find():
	print(i)
