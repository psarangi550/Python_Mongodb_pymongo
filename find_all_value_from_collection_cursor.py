from pymongo import MongoClient

#local connection
conn=MongoClient(host="localhost",port=27017)

#creating the db
db=conn.school

#creating the collection
collection=db.students

#fetching the cursor using the find ()

all_docs=collection.find({"std":5})

# for doc in all_docs:
#     print(doc)
    
#prettyprinting it 
from pprint import pprint

#for python3.8 onwards 

# for doc in all_docs:
#     pprint(doc,sort_dicts=False)

#for python 3.7 less

def new_func(x):
    return x

pprint._sorted=new_func


# for doc in all_docs:
#     pprint(doc)

for doc in all_docs:
    pprint(doc,width=30)
    print()
