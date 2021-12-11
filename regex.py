# regex pattern matching for emails
def isValidEmail(s):       
    import re
    return False if not re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{1,3}$',s) else True

def slice(s, n):
    from textwrap import wrap
    return wrap(s, n)
