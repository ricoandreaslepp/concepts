# regex pattern matching for emails
def isValidEmail(s):       
    import re
    return False if not re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{1,3}$',s) else True

def slice(s, n):
    from textwrap import wrap
    return wrap(s, n)

# currently only works <=1000
# returns a list
def num2words(n):
    
    import re

    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    decine = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    result = []
    s = str(n)
    while True:
        
        if n==1000:
            result = ["one", "thousand"]
            break
            
        elif n >= 100:
            result.append(digits[int(s[0])])
            result.append("hundred")
            
            if sum(map(int, s[1:])) != 0:
                result.append("and")
            
        elif n >= 20:
            result.append(decine[int(s[0])-2])
                
        elif n > 0:
            result.append(digits[n])
            break
    
        s = str(n)[1:]
        n = int(s)
        
        if not s:
            break
    
    return result
