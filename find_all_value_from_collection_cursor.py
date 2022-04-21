from pymongo import MongoClient

#local connection
conn=MongoClient(host="localhost",port=27017)

#creating the db
db=conn.school

#creating the collection
collection=db.students

#fetching the cursor using the find ()

all_docs=collection.find({})

# for doc in all_docs:
#     print(doc)
    
#prettyprinting it 
from pprint import pprint

for doc in all_docs:
    pprint(doc,sort_dicts=False)
