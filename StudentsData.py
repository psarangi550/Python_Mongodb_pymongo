import pymongo
from pymongo import MongoClient
c = MongoClient('localhost', 27017)
db = c.schoolnew
col = db.students
col.drop()
col = db.students
import pprint
pp = pprint.PrettyPrinter(width = 30, sort_dicts = False)
a = [{"rollNo" : 51, "gender" : "F", "std" : 5, "games" : ["baseball", "skiing", "chess"], "charges" : 25,
      "name" : {"first" : "julia",
              "last" : "roberts"
             }
     },
     {"rollNo" : 63, "gender" : "M", "std" : 6, "games" : ["cricket", "skiing"], "charges" : 35,
      "name" : {"first" : "donald",
              "last" : "trump"
             }
     },
     {"rollNo" : 55, "gender" : "M", "std" : 5, "games" : ["skiing", "football"], "charges" : 20,
      "name" : {"first" : "boris",
              "last" : "baker"
             }
     },
     {"rollNo" : 53, "gender" : "F", "std" : 5, "games" : ["baseball", "volleyball"], "charges" : 25,
      "name" : {"first" : "dolly",
              "last" : "parton"
             }
     },
     {"rollNo" : 61, "gender" : "F", "std" : 6, "games" : ["skiing", "handball"], "charges" : 30,
      "name" : {"first" : "diana",
              "last" : "spencer"
             }
     },
     {"rollNo" : 62, "gender" : "F", "std" : 6, "games" : ["skiing", "carrom"], "charges" : 35,
      "name" : {"first" : "martina",
              "last" : "navratilova"
             }
     },
     {"rollNo" : 52, "gender" : "M", "std" : 5, "games" : ["baseball", "hockey"], "charges" : 20,
      "name" : {"first" : "george",
              "last" : "bush"
             }
     },
     {"rollNo" : 65, "gender" : "M", "std" : 6, "games" : ["handball", "skiing", "chess"], "charges" : 35,
      "name" : {"first" : "barack",
              "last" : "obama"
             }
     },
     {"rollNo" : 54, "gender" : "F", "std" : 5, "games" : ["baseball", "skiing", "chess"], "charges" : 25,
      "name" : {"first" : "ivanka",
              "last" : "trump"
             }
     },
     {"rollNo" : 64, "gender" : "M", "std" : 6, "games" : ["handball", "chess"], "charges" : 35,
      "name" : {"first" : "bill",
              "last" : "clinton"
             }
     },
     {"rollNo" : 71, "gender" : "F", "std" : 7, "games" : ["tennis", "skiing"], "charges" : 40,
      "name" : {"first" : "hillary",
              "last" : "clinton"
             }
     },
     {"rollNo" : 57, "gender" : "F", "std" : 5, "games" : ["baseball", "skiing"], "charges" : 25,
      "name" : {"first" : "martina",
              "last" : "hingis"
             }
     },
     {"rollNo" : 74, "gender" : "F", "std" : 7, "games" : ["baseball", "skiing"], "charges" : 35,
      "name" : {"first" : "oprah",
              "last" : "winfrey"
             }
     },
     {"rollNo" : 58, "gender" : "M", "std" : 5, "games" : ["baseball", "chess"], "charges" : 20,
      "name" : {"first" : "peter",
              "last" : "anderson"
             }
     },
     {"rollNo" : 73, "gender" : "F", "std" : 7, "games" : ["tennis", "skiing", "football"], "charges" : 25,
      "name" : {"first" : "rebecca",
              "last" : "mark"
             }
     },
]

n = col.insert_many(a)
print(n.acknowledged)
