# Team_2 Haonan Di, Yuxin Hu, Singh Shashank
import re

file_loc = 'expenses.txt'

with open(file_loc, 'r') as f:
    records = [line.rstrip() for line in f]

# part a)
# pat = r'D'

# part b)
# pat = r'\''

# part c)
# pat = r"\""


# part d)
# pat = '7.*'


# part e)
# pat = '[rt]$'  # use $ to match the end of the string


# part f)
# pat = r'\.'

# part g)
# pat = 'r[^g]*g'


# part h)
# pat = '[A-Z][A-Z]'


# part i)
# pat = r','


# part j)
# pat = ',[^,]*,[^,]*,'


# part k)
# pat = r'^[^vwxyz]*$'

# part l)
# pat = '^[1-9][0-9]\\.'


# part m)
# add the begin and end signal
# pat = '^[^,]*,[^,]*,[^,]*,[^,]*$'


# part n)
# pat = '\\('


# part o)
# pat = '^[1-9][0-9][0-9]\\..*:meal'


# part p)
# we assume that the new category do not contain number
# pat = '^[1-9][0-9]*\\.[0-9]{2}:[a-zA-Z]{4}:'


# part q)
# pat = ':[0-9]{4}03[0-9]{2}:'


# part r)
# pat = 'a.*b.*c'


# part s)
# pat = r'(..).*\1.*\1'


# part t)
# match from the end
# pat = 'a[^:]*[0-9][^:]*$|[0-9][^:]*a[^:]*$'


# part u)
# pat = '^[^A-Z]*$'


# part v)
# pat = 'd[a-zA-Z]?i'

for line in records:
    if re.search(pat, line) != None:
        print(line)
