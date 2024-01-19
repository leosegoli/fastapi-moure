from pymongo import MongoClient

#base de datos local
#db_client = MongoClient().local

#base de datos remota
db_client = MongoClient("").test
