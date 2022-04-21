from pymongo import MongoClient
#creating the connection object
conn=MongoClient(host="localhost",port=27017)

#creating the db object from the connection object 
db=conn["school"]

#creating the collection object as 
collection=db["students"]

#building the query as below
query={"std":7}

#here we want to see the field as  
fields_filter={"rollNo":1,"_id":0,"charges":1,"name":1}

#here if we want to limit the value to 2
# all_docs=collection.find(query,fields_filter).sort("name.last",-1).limit(2)

#here if we want to skip the 1st document
all_docs=collection.find(query,fields_filter).sort("name.last",-1).skip(2)



#fetching the cursor which will display the documents in the collection
# all_docs=collection.find(query,fields_filter).sort("name.last",-1)

#pretty print option
import pprint
pp=pprint.PrettyPrinter(width=30,sort_dicts=False)

#printing the sorted value as
for doc in all_docs:
    pp.pprint(doc)
    print()

