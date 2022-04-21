from pymongo import MongoClient
# localmongodb setup connection
conn=MongoClient(host="localhost",port=27017)
if conn is not  None:
    print("connection successful")
else:
    print("something went wrong")

#creating the db object  from the connection object 
db=conn.school
#creating the collection object from the db object 
collection=db.students
#fetching a data in the form of the query as
query={"std":5}
#using the find_one() fetch a particular object 
# print(collection.find_one(query))


#for making it pretty printed then we need to use pprint module 
import pprint
#now qw need to use the pprint() of the pprint module  as below 
#here the result will come in a  sorted manner
# pprint.pprint(collection.find_one(query))

#if we want the result aas it is then we need to use below format 
#pprint module has PrettyPrinter class , we can create the object of that , to which we can pprint()
#using the sort_dict to  False in order to use this method 
pp=pprint.PrettyPrinter(sort_dicts=False)
data=collection.find_one(query)
pp.pprint(data)
# pprint.pprint(data,sort_dicts=False)
# pprint.pprint(help(pprint.PrettyPrinter))

