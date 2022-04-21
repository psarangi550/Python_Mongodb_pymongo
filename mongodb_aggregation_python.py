from pymongo import MongoClient

import pprint

conn=MongoClient(host="localhost",port=27017)

db=conn.school

col=db.students

pp=pprint.PrettyPrinter(width=40,sort_dicts=False)

# all_docs=col.find({})

# for doc in all_docs:
#     pp.pprint(doc)
#     print()

#using the aggregation for the same

# query=[
    
#     {
#         "$match":{"gender":"F"}
#     },
#     {
#         "$group":{"_id":{"standard":"$std"},"total_count":{"$sum":1}}
#     }
# ]


# all_docs_aggr=col.aggregate(query)

# for doc in all_docs_aggr:
#     pp.pprint(doc)
#     print()
    
    
#another aggregation

# query=[
    
#     {
#         "$match":{"gender":"F"}
#     },
#     {
#         "$group":{"_id":{"standard":"$std","gender":"$gender"},"total_count":{"$sum":"$charges"}}
#     }
# ] 

# all_docs_aggr=col.aggregate(query)

# for doc in all_docs_aggr:
#     pp.pprint(doc)
#     print()

# sorting it in the desending order using $sort operator 

# query=[
    
#     {
#         "$match":{"gender":"F"}
#     },
#     {
#         "$group":{"_id":{"standard":"$std","gender":"$gender"},"total_count":{"$sum":"$charges"}}
#     },
#     {
#         "$sort":{"_id.standard":-1}
#     }
# ] 

# all_docs_aggr=col.aggregate(query)

# for doc in all_docs_aggr:
#     pp.pprint(doc)
#     print()



#using the $unwind operator with aggregation expression 

# query=[
#     {
#         "$unwind":"$games"
#     },
#     {
#         "$group":{"_id":{"standard":"$std","gender":"$gender"},"games_per_gender":{"$addToSet":"$games"}}
#     }
# ] 

# all_docs_aggr=col.aggregate(query)

# for doc in all_docs_aggr:
#     pp.pprint(doc)
#     print()


#using the $unwind operator with aggregation expression with the sort 

query=[
    {
        "$unwind":"$games"
    },
    {
        "$group":{"_id":{"standard":"$std","gender":"$gender"},"games_per_gender":{"$addToSet":"$games"}}
    },
    {
        "$sort":{"_id.gender":-1}
    }
] 

all_docs_aggr=col.aggregate(query)

for doc in all_docs_aggr:
    pp.pprint(doc)
    print()
    

