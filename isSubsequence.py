def isSubsequence(s : "where to look from", t : "what to look for") -> "True or False":

    i, j = 0, 0
    
    while i < len(s) and j < len(t):
        if s[i]==t[j]:
            j += 1
        i += 1

    # if j reached the end of string t
    return j==len(t)
  
s, t = input("Whole string: "), input("Sequence to check: ")
print("%s %s a subsequence of %s" % (t, "is" if isSubsequence(s, t) else "is not", s))
