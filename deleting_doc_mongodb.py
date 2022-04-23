from unittest import result
from pymongo import MongoClient #importing the MongoClient class from the pymongo module
import pprint #importing the pprint module 
#creating the connection object 
conn=MongoClient(host="localhost",port=27017)
#connecting to the db studentnew
db=conn.schoolnew
#connecting to the collection col as
col=db.students
#using the prettyprint option for showing it design based
pp=pprint.PrettyPrinter(width=30,sort_dicts=False)

#now we can use the delete_one to delete a particular element as
# result=col.delete_one({"rollNo":75}).deleted_count

#now we can also check deleted count from there as 

# print(result)

#deleting multiple documents using the delete_many option as

result=col.delete_many({"charges":{"$gt":30}}).deleted_count

print(result)

