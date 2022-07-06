def isSubsequence(s : "where to look from", t : "what to look for") -> "True or False":

    i, j = 0, 0
    
    while i < len(s) and j < len(t):
        if s[i]==t[j]:
            j += 1
        i += 1

    # if j reached the end of string t
    return j==len(t)
  
# regex pattern matching for emails
def isValidEmail(s : "email string") -> "True or False email":
    import re
    return False if not re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+.[a-zA-Z]{1,3}$',s) else True

# from textwrap official docs:
# Wraps the single paragraph in text so every line is at most width characters long. .
def slice(s : "input string", n : "width of line") -> "a list of output lines, without final newlines":
    from textwrap import wrap
    return wrap(s, width)

def matchGenerator(s : "input string", k : "input pattern") -> "match object or None":
    import re

    pattern = re.compile(k)
    r = pattern.search(s)
    while 1:
        yield r # returns None when no more matches are found
        r = pattern.search(s, r.start()+1)

if __name__=='__main__':

    """ # Example usage of the matchGenerator function
    match = matchGenerator("terete", "te")
    while (x:=next(match)):
        print(x)
    """


    """ # Example usage of the isSubsequence function
    s, t = input("Whole string: "), input("Sequence to check: ")
    print("%s %s a subsequence of %s" % (t, "is" if isSubsequence(s, t) else "is not", s))
    """
