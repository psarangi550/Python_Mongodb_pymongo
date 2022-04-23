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

#fetching all the elements 
# for doc in col.find({}):
#     pp.pprint(doc)


insert_list=[{
 'rollNo': 65,
 'gender': 'F',
 'std': 7,
 'games': ['tennis',
           'skiing',
           'football',
           'cricket'],
 'charges': 45,
 'name': {'first': 'rika',
          'last': 'sarangi'},
 'transport': 35
},
{
 'rollNo': 85,
 'gender': 'F',
 'std': 6,
 'games': ['tennis',
           'skiing',
           'football'
           ],
 'charges': 75,
 'name': {'first': 'rika',
          'last': 'sarangi'},
 'transport': 45
}
]

#inserting the document into the student document using the insert_one option as
# pushed_id=col.insert_one({
# 'rollNo': 75,
# 'gender': 'F',
# 'std': 7,
# 'games': ['tennis',
# 'skiing',
# 'football',
# 'cricket'],
# 'charges': 45,
# 'name': {'first': 'abismruta',
# 'last': 'sarangi'},
# 'transport': 25
# }).inserted_id

#printing the id of the inserted document
# print(pushed_id)

#quering using the pushed_id as 
# pp.pprint(col.find_one({"rollNo":75}))

#using the insert_many to add a list of documents to the collection as



#using the insert many to add a List of documents into the collection
result=col.insert_many(insert_list).inserted_ids

#now here also i can see the id which being in the list format as
print(result)

for doc in col.find({}):
    pp.pprint(doc)