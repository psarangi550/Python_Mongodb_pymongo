# from email import iterators
# import re #importing the re module 
#finding the iterators from the pattern
# matcher_list=re.findall('bc',"abcdefg7@9bcfd")
#another approach 
# pattern=re.compile('bc')
#fetching the matcher using the pattern
# matcher=pattern.finditer("abcdefg7@9bcfd")
#iterating over the matcher
#counting the value 
# count=0
# for match in matcher:
#     print(f'{match.start()}-------------{match.group()}')
#     count+=1
# print(f"The total count is {count}")

# for item in matcher_list:
#     print(item)

# print(matcher_list)

#using the subn() of the re module 
# result_str,replacement=re.subn("bc","#","abcdefg7@9bcfd")

# print(result_str)
# print(replacement)

import re

# pattern="[a-k][369][a-zA-Z0-9]*"

# target_string=input("Enter a String")

# match=re.fullmatch(pattern,target_string)

# if match is not None:
#     print("valid yava language")
# else:
#     print("Not a valid one")


#10 and 11 digit number checking 

pattern="(\+91|0)?[6-9][0-9]{9}"

target_string=input("Enter a String")

match=re.fullmatch(pattern,target_string)

if match is not None:
    print("valid phone number")
else:
    print("Not a valid phone number")

