from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['stackoverflow']
# collection_questions = db['questions']
collection_space = db['space']
# for i in collection_questions.find().limit(100):
# collection_space.insert(i)

for i in collection_space.find():
    array = i['status']
    print(type(array))