import re

# regex pattern matching for emails
def isValidEmail(s):       
    e = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{1,3}$',s)
    return True if e != None else False
