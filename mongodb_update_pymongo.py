# import queue
from pymongo import MongoClient #importing the MongoClient class from the pymongo module
import pprint #importing the pprint module 
#creating the connection object 
conn=MongoClient(host="localhost",port=27017)
#connecting to the db studentnew
db=conn.schoolnew
#connecting to the collection col as
col=db.students

#creating the pp object of PrettyPrinter class to display nicely
pp=pprint.PrettyPrinter(width=30,sort_dicts=False)

#fetchign all the document as 
# for doc in col.find({}):
#     pp.pprint(doc)
#     print()
    
#using the upsert option to update if the data available if not then insert
# query={"rollNo":59}

#using the update_one method query are



#using to find the value 
# pp.pprint(col.find_one(query))#None
# update_info={
#     "$set":{
#         "gender":"F",
#         "name":{
#             "first":"rika",
#             "last":"abi"
#         }
#     }
# }


#here we need to use the update_one method with upsert operation as 
# result=col.update_one(query,update_info,True)
#now fetchign the ackownledged as 
# print(result.acknowledged)
#fetching the updated data using the find_one()
# pp.pprint(col.find_one(query))

#incrementing the value to the $inc and setting the name to malena

# new_query={"rollNo":54}

#fetching the data as 

# pp.pprint(col.find_one(new_query))

#update query as 

# update_info={
#     "$set":{
#         "name.first":"malena"
#     },
#     "$inc":{
#         "charges":5
#     }
# }

#now using the update query without the upsert as
# result=col.update_one(new_query,update_info)
#here we can check the query as
# pp.pprint(col.find_one(new_query))

#setting the transport amount to document and pusing the baseball value to the document as 

# update_info={
#     "$set":{
#         "transport":20
#     },
#     "$push":{
#         "games":"baseball"
#     }
# }

# result=col.update_one(new_query,update_info)
#feting the acknowlegment 
# print(result.acknowledged)
#fetching the query as
# pp.pprint(col.find_one(new_query))


#now we can see the same query with $addToSet operator 

# update_info={
#     "$addToSet":{
#         "games":"chess"
#     }
# }

# result=col.update_one(new_query,update_info)
# #feting the acknowlegment 
# print(result.acknowledged)
# #fetching the query as
# pp.pprint(col.find_one(new_query))

#using the $pull Operator to remove baseball from the last as
#here removing the base ball from the array as the first Element
# update_info={
#     "$pop":{
#         "games":-1 
#     }
# }

# result=col.update_one(new_query,update_info)
# #feting the acknowlegment 
# print(result.acknowledged)
# #fetching the query as
# pp.pprint(col.find_one(new_query))

#removing the chess using the $pull operator as

# update_info={
#     "$pull":{
#         "games":"chess" 
#     }
# }

# result=col.update_one(new_query,update_info)
# #feting the acknowlegment 
# print(result.acknowledged)
# #fetching the query as
# pp.pprint(col.find_one(new_query))

#here we can also the option for the update_many for std=7 as below

query={"std":7}

#fetching the doc as 
# pp.pprint(col.find(query))

# for doc in col.find(query):
#     pp.pprint(doc)

#update info for std 7 i.e setting the transport as 20 incrementing the charges by 5 and adding the game as cricket and skiing 

update_info=\
    {
    "$set":{
        "transport":20
    },
    "$inc":{
        "charges":5
    },
    "$addToSet":{"games":
        {
            "$each":["cricket","skiing"]
        }
    }
}

# #now using the update_many query as
result=col.update_many(query,update_info)

# #here using the info  to see how many record changes we can use modified_count as
print(result.modified_count)

# #now fetching the value for the all

for doc in col.find(query):
    pp.pprint(doc)



