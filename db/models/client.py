from pymongo import MongoClient

#base de datos local
#db_client = MongoClient().local

#base de datos remota
db_client = MongoClient("mongodb+srv://test:test@cluster0.ca8nycl.mongodb.net/?retryWrites=true&w=majority").test