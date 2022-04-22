import re #importing the re module 
import pprint #importing the pprint module 
from pymongo import MongoClient #importing the MongoClient class from pymongo module 
#creating the connection object 
conn=MongoClient(host="localhost",port=27017)
#now we need to use the db object for the same as 
db=conn.school
#creating the collection object as col
col=db.students
#fetching all the docs using the pprint module as below 
pp=pprint.PrettyPrinter(width=30,sort_dicts=False)
#iterating through the documents
# for doc in col.find({}):
#     pp.pprint(doc)
#now using the mongodb regular expresion using the re module as 
# query={"name.first":re.compile("^re")}

query={"name.first":{"$regex":"^re"}}


query={"name.first":{"$regex":"^re","$option":"i"}}

for doc in col.find(query):
    pp.pprint(doc)