
import re 

file_loc = r'D:\project_agg\21S_DFP_project\Lec5\expenses.txt'

def readin(file_loc):
    tmp = [lines for lines in open(file_loc, 'rt', encoding='UTF-8')]
    for i in range(len(tmp)):
        tmp[i] = tmp[i][:-1]
    return tmp #any more efficient way?

def search_key_word(records, key_word, pattern = 'search'):
    print('') #print a blank line to separate
    if pattern != 'search':
        for line in records:
            if re.match(key_word, line) != None:
                print(line)
    else:
        for line in records:
	        if re.search(key_word, line) != None:
	            print(line)
    

records = readin(file_loc)
# part a)
pat = r'D'
search_key_word(records, pat)

# part b)
pat = r'\''
search_key_word(records, pat)

# part c)
pat = r"\""
search_key_word(records, pat)

# part d)
pat = '7.*'
search_key_word(records, pat, 'match')

# part e)
pat = '[rt]$' # use $ to match the end of the string
search_key_word(records, pat)

# part f)
# a literal period . should be the . in the context?
# in this case the . in 79.81 do not count
pat = '\d+\\.\d+[^\\.]*\\.'
search_key_word(records, pat)

# part g)
pat = 'r[^g]*g'
search_key_word(records, pat)

# part h)
pat = '[A-Z][A-Z]'
search_key_word(records, pat)

# part i)
pat = ','
search_key_word(records, pat)

# part j)
pat = ',[^,]*,[^,]*,'
search_key_word(records, pat)

# part k)
print('')
for line in records:
    pat = '[^vwxyz]' + '{' + str(len(line)) + '}'
    if re.match(pat, line) != None:
        print(line)

# part l)
pat = '^[1-9][0-9]\\.'
search_key_word(records, pat)

# part m)
# add the begin and end signal
pat = '^[^,]*,[^,]*,[^,]*,[^,]*$'
search_key_word(records, pat, 'match')

# part n)
pat = '\\('
search_key_word(records, pat)

# part o)
pat = '^[1-9][0-9][0-9]\\..*:meal'
search_key_word(records, pat)

# part p)
# we assume that the new category do not contain number
pat = '^[1-9][0-9]*\\.[0-9]{2}:[a-zA-Z]{4}:'
search_key_word(records, pat, 'match')

# part q)
pat = ':[0-9]{4}03[0-9]{2}:'
search_key_word(records, pat)

# part r)
pat = 'a.*b.*c'
search_key_word(records, pat)

# part s)
pat = r'(..).*\1.*\1'
search_key_word(records, pat)

# part t)
# match from the end
pat = 'a[^:]*[0-9][^:]*$|[0-9][^:]*a[^:]*$'
search_key_word(records, pat)

# part u)
pat = '^[^A-Z]*$'
search_key_word(records, pat)

# part v)
pat = 'd[a-zA-Z]?i'
search_key_word(records, pat)

