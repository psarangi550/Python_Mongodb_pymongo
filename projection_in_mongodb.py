from pymongo import MongoClient
# localmongodb setup connection
conn=MongoClient(host="localhost",port=27017)

#creating the db
db=conn["school"]

#creating the collection
collection=db["students"]

#query here to fetch the std:5 value
query={"std":5}

#here we want to see the field as  
fields_filter={"rollNo":1,"_id":0,"charges":1}

#now using the cursor as  find() with query and find_filter
all_req_docs=collection.find(query,fields_filter)

#now iterating over it as
from pprint import pprint

for doc in all_req_docs:
    pprint(doc, width=40, sort_dicts=False)


