from pymongo import MongoClient
# localmongodb setup connection
# conn=MongoClient(host="localhost",port=27017)
# if conn is not  None:
#     print("connection successful")
# else:
#     print("something went wrong")
# #remote host connection 
# conn=MongoClient(host="150.230.142.239",port=27017)
# if conn is not  None:
#     print("connection successful")
# else:
#     print("something went wrong")

# import pprint
from pprint import pprint,PrettyPrinter
# # print(pprint.pprint())
# # import collections.abc
# check=hasattr(pprint.PrettyPrinter , "pprint")
# print(check)
check=isinstance(pprint,PrettyPrinter)
print(check)