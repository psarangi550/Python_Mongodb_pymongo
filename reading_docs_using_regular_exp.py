from ast import match_case
import re #importing the re module

pattern="(\+91|0)?[6-9][0-9]{9}"

email_pattern="\w[a-zA-Z0-9._]*@gmail[.]com"

f2=open("output.txt","w")

# with open("fetch.txt","r") as f1:
#     data=f1.read()
#     match_iter=re.finditer(pattern,data)
#     for match in match_iter:
#         if match is not  None :
#             f2.write(match.group()+"\n")
#         else:
#             print("No Match Found")
#     f2.close()
    

with open("fetch.txt","r") as f1:
    data=f1.read()
    match_iter=re.finditer(email_pattern,data)
    for match in match_iter:
        if match is not  None :
            f2.write(match.group()+"\n")
        else:
            print("No Match Found")
    f2.close()

    