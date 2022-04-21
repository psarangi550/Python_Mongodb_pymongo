from pymongo import MongoClient

#local connection
conn=MongoClient(host="localhost",port=27017)

#creating the db
db=conn.school

#creating the collection
collection=db.students

#fetching the total count of documents in the collection 
print(collection.count_documents(filter={}))

#preparing the query as 
query={"std":6}

#fetching the collection value based on a query is 
print(collection.count_documents(filter=query))