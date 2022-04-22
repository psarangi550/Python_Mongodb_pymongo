# from ast import pattern
import re
import urllib
import urllib.request
import pprint
# pattern="(\+91|0)?[6-9][0-9]{9}"
email_pattern="\w*@gmail.com"
site="https://jntuh.ac.in/contact-us#"
resp=urllib.request.urlopen(site)
byte_text=resp.read()
text=byte_text.decode()
# matcher=re.finditer(pattern,text)
#duplicated value
# matcher=re.finditer(email_pattern,text)
# for match in (matcher):
#     print(match.group())
#remove duplicates
matcher=set(re.findall(email_pattern,text))
for match in (matcher):
    print(match)
