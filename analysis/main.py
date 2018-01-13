import anaplysis_tag
import analysis_counts
from pymongo import MongoClient
import json
import read


# 库名：出现次数
packageCounts = {}
# 库名：热度
packageStatus = {}
# （库名1，库名2）：次数
packageRelationship = {}
# （库名：描述）
packageDescription = {}
# 建立数据库连接
client = MongoClient('localhost', 27017)
db = client['stackoverflow']
collection_questions = db['questions']
# collection_space = db['space']
# for i in collection_questions.find().limit(100):
# collection_space.insert(i)

packageCounts = analysis_counts.getCounts(collection_questions)
packageRelationship = anaplysis_tag.getRelationship(collection_questions, read.getPackageList())

