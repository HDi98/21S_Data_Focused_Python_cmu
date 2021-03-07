

expense_file_location = 'E:/project_agg/DFP_project/Lec3/expenses.txt'
records =[]

# 1.a read in and store the line in records in list records
fin = open(expense_file_location, 'rt', encoding='UTF-8')
for lines in fin:
    '''the lines must be processed to avoid the \\n in lines'''
    lines = lines[:-1]
    records += [lines]

for line in records:
    print(line)
# print(records)

# 1.b list comprehension notation to generate records2
fin.close()

fin2 = open(expense_file_location, 'rt', encoding='UTF-8')
records2 = [lines[:-1] for lines in fin2]
print("\nrecords == records2:",records == records2, '\n')

# 1.c tuple of tuples
fin2.close()

fin3 = open(expense_file_location, 'rt', encoding='UTF-8')
records3 = [tuple(lines[:-1].split(':')) for lines in fin3]
records3 = tuple(records3)
for tup in records3:
    print(tup)

fin3.close()

# 1.d split the categories and dates

cat_set = set()
date_set = set()
for tup in records3:
    cat_set.add(tup[1])
    date_set.add(tup[2])

#header should not be included
cat_set.remove('Category')
date_set.remove('Date')

print('\nCategories:', cat_set, '\n')
print('Dates:     ', date_set, '\n')

# 1.e
# print(len(records3))
# print(records3[4])

rec_num_to_record = {}
for i in range(len(records3)):
    rec_num_to_record[i] = records3[i]

#print(len(rec_num_to_record))
for rn in range(len(rec_num_to_record)):
	print('{:3d}: {}'.format(rn, rec_num_to_record[rn]))

print("\nThis is output using items iterable")
for i in rec_num_to_record.items():
	print('{:3d}: {}'.format(i[0], i[1]))

print("\nThis use tuple unpacking method")
for k, v in rec_num_to_record.items():
	print('{:3d}: {}'.format(k, v))

## for me, I will use the keys() and values() to display the dictionary.