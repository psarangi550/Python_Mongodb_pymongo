from pymongo import MongoClient #importing the MongoClient from pymongo module 
import pprint #importing the pprint module 
#connectr to the Mongodb Server 
conn=MongoClient(host="localhost",port=27017)
#creating the db object 
db=conn.school
#creating the collection 
col=db.students
#now using the pprint to display in a beautiful way
pp=pprint.PrettyPrinter(width=30,sort_dicts=False)

#now using the mongo db query with condition as below 
# query={"charges":{"$gt":25}}

#now using the query with the  find() as
# all_doc=db.students.find(query)

#now we can use the documents in the cursor in order to display as below 

# for doc in all_doc:
#     pp.pprint(doc)

#now using the $ne see the value where the charges not equal to 35

# query={"charges":{"$ne":35}}

# all_doc=db.students.find(query)

# for doc in all_doc:
#     pp.pprint(doc)


#using the  $in operator for the same column  value as or operator 

# query={"charges":{"$in":[30,40]}}

# all_doc=db.students.find(query)

# for doc in all_doc:
#     pp.pprint(doc)

#using the  $in operator with the array as 

# query={"games":{"$in":["tennis","handball"]}}

# all_doc=db.students.find(query)

# for doc in all_doc:
#     pp.pprint(doc)

#using the  $nin operator with the array as 

# query={"games":{"$nin":["tennis","handball"]}}

# all_doc=db.students.find(query)

# for doc in all_doc:
#     pp.pprint(doc)

#now using the $all operator as 

# query={"games":["baseball","skiing"]}

# all_doc=db.students.find(query)

# for doc in all_doc:
#     pp.pprint(doc)
    

#no output as we change the order

# query={"games":["skiing","baseball"]}

# all_doc=db.students.find(query)

# for doc in all_doc:
#     pp.pprint(doc)

#using the $all operator for the same 

# query={"games":{"$all":["skiing","baseball"]}}

# all_doc=db.students.find(query)

# for doc in all_doc:
#     pp.pprint(doc)

#using the $or operator as

# query={"$or":[{"name.first":"donald"},{"name.last":"bush"}]}

# all_doc=db.students.find(query)


# for doc in all_doc:
#     pp.pprint(doc)