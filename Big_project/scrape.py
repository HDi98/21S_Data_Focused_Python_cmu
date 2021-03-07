from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
import re 


html = urlopen('https://www.siliconvalleypower.com/residents/save-energy/appliance-energy-use-chart')

bsyc = BeautifulSoup(html.read(), "lxml")

fout = open('bsyc_temp.txt', 'wt', encoding='utf-8')

fout.write(str(bsyc))

fout.close()

table_list = bsyc.findAll('table')


print('there are', len(table_list), 'table tags')
# there are three table tags

for t in table_list:
    print(str(t)[:100])

main_table_lst = bsyc.findAll('table', {'class': 'tableData'})
print(len(main_table_lst))

main_table = main_table_lst[0]
# print(str(main_table))

# write into a list to output file
# output should be a 5 columns data: demo_out = ['', '', '', '', '']
out = [] #list of lists, in which every list is a line

for tr in main_table.select('tr'):
    print(str(tr))
    tmplst1 = []
    for td in tr.select('td'):
        print(str(td.contents), ' End of this print')
        if len(str(td)) > 1:
            try:
                tmplst1 += [str(td.contents[0])]
            except:
                tmplst1 += []
    print(tmplst1, '\n')


#     if len(c) > 1:
#         for r in c.children:
#             # extract a lot of length 1
#             if len(r) > 1:
#                 # one r is one row in chart
#                 # print(r.contents)
#                 print(len(r.contents))
#                 header1 = ''  #Big header
#                 header2 = '' #second header, may be not existed
#                 if len(r.contents) == 3:  # 标题或空行
#                     header1 = ''
#                     header2 = ''
#                     # define the header1 and header2
#                     for new in r.contents:
#                         if new != '\n':
#                             if new.contents[0] == '\n' and new.contents[2] == '\n':
#                                 header1 = new.contents[1].contents[0]
#                                 continue 
#                             for j in new.contents:
#                                 if re.search(r'<strong>(.*)<\strong>', j) != None:
#                                     tmp = re.search(r'<strong>(.*)<\strong>', j)





#                 if len(r.contents) == 9: #formal line
                

                


#                 for new in r.contents:
#                     if new != '\n':
#                         print(new.contents) # in this part finally find the data, can use index to locate it
#                 # for new in r.children:
#                 #     print(new.contents)
#             #print(str(r)[:100], 'length for this r:', len(r))
