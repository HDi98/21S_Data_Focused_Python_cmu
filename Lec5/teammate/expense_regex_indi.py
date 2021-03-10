'''
TEAM 2 - HW 5
@author: Shashank Kumar Singh
         Di,Haonan
         Hu,Yuxin
Andrew Id : sksingh2
            hdi
            yuxinhu
'''

import re 

recFile=open("expenses.txt","rt")

records=[line[:-1] for line in recFile.readlines()]

def search_key_word(records, key_word):
    
    print('') #print a blank line to separate
    
    for line in records:
        if re.search(key_word, line) != None:
            print(line)

'''
# part 1a)
pat = r'D'
search_key_word(records, pat)

# part 1b)
pat = r'\''
search_key_word(records, pat)

# part 1c)
pat = r"\""
search_key_word(records, pat)

# part 1d)
pat = r'^7'
search_key_word(records, pat)

# part 1e)
pat = r'[rt]$' # use $ to match the end of the string
search_key_word(records, pat)

# part 1f)
# a literal period . should be the . in the context?
# in this case the . in 79.81 do not count
pat=r':.*\..*$'
search_key_word(records, pat)

# part 1g)
pat = r'r[^r]*g' 
search_key_word(records, pat)

# part 1h)
pat = r'[A-Z][A-Z]'
search_key_word(records, pat)

# part 1i)
pat = r','
search_key_word(records, pat)

# part 1j)
#pat = r',[^,]*,[^,]*,'
search_key_word(records, pat)

# part 1k)
pat = r'^[^vwxyz]*$'
search_key_word(records, pat)

# part 1l)
pat = r'^[1-9][0-9]\.[0-9][0-9][:]'
search_key_word(records, pat)

# part 1m)
# add the begin and end signal
pat = r'^[^,]*(,[^,]*){3}$'
search_key_word(records, pat)

# part 1n)
pat = r'\('
search_key_word(records, pat)

# part 1o)
pat = r'^[1-9][0-9][0-9]\..*:meal:.*'
search_key_word(records, pat)

# part 1p)
# we assume that the new category do not contain number
pat = r'[0-9]:[a-zA-Z]{4}:'  
search_key_word(records, pat)

# part 1q)
pat = r'.*:.*:[0-9]{4}03[0-9]{2}:' 
search_key_word(records, pat)

# part 1r)
pat = r'a.*b.*c'
search_key_word(records, pat)

# part 1s)
pat = r'(..).*\1.*\1'
search_key_word(records, pat)

# part 1t)
# match from the end
pat = r'a[^:]*[0-9][^:]*$|[0-9][^:]*a[^:]*$'
search_key_word(records, pat)

# part 1u)
pat = r'^[^A-Z]*$'
search_key_word(records, pat)
'''

# part 1v)
pat = r'd.?i'
search_key_word(records, pat)

