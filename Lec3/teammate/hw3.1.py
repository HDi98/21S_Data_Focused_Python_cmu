# Part a
records = []
with open('expenses.txt', 'r') as in_f:
    for line in in_f:
        records.append(line.strip())
    for line in records:
        print(line)

# Part b
with open('expenses.txt', 'r') as in_f:
    records2 = [line.strip() for line in in_f]
    print("\nrecords == records2:", records == records2, '\n')

# Part c
with open('expenses.txt', 'r') as in_f:
    records3 = tuple([tuple(line.strip().split(":")) for line in in_f])
    for tup in records3:
        print(tup)

# Part d
cat_set = {tup[1] for tup in records3 if tup[1] != 'Category'}
date_set = {tup[2] for tup in records3 if tup[2] != 'Date'}
print('Categories:', cat_set, '\n')
print('Dates:     ', date_set, '\n')

# Part e
rec_num_to_record = {k: v for k, v in zip(range(len(records3)), records3)}
for k, v in rec_num_to_record.items():
    print('{:3d}: {}'.format(k, v))
