import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
import re 
import seaborn as sns
plt.style.use('seaborn-whitegrid')
sns.set_theme(style="whitegrid")

import webscrape

class suggestion:

    def __init__(self):
        return 
    
    def readdata(self, filename, sheetname):
        '''clean data for this part should be a xlsx file so we must specify the filename and sheetname'''
        #try:
        graph = pd.read_excel(filename, sheet_name=sheetname, engine='openpyxl')
        # except:
        #     print(filename)
        #     print("filename or sheetname is wrong, Please check your input")
        #     return 
            
        graph = graph[:-6]  #delete the last six lines which is the comment
        
        graph['ESTIMATED ENERGY USAGE*'] = graph['ESTIMATED ENERGY USAGE*'].apply(lambda x: x.split(' ')[0])
        graph['ESTIMATED ENERGY COSTS**'] = graph['ESTIMATED ENERGY COSTS**'].apply(lambda x: x.split(' ')[0][1:])
        graph['ESTIMATED ENERGY COSTS**'] = graph['ESTIMATED ENERGY COSTS**'].apply(lambda x: x.split('/')[0])
        
        for i in range(len(graph['CATEGORY1'])):

            # the column estimated energy costs is cleaned in this process
            # print(graph['ESTIMATED ENERGY COSTS**'][i])
            
            if '$' in graph['ESTIMATED ENERGY COSTS**'][i]:
                # print("I come into the if statment")
                tmp = graph['ESTIMATED ENERGY COSTS**'][i].split('–$')
                graph['ESTIMATED ENERGY COSTS**'][i] = (float(tmp[0]) + float(tmp[1])) / 2
            elif graph['ESTIMATED ENERGY COSTS**'][i] == 'ess':            
                # catch the exception when less than 0.01 per use
                graph['ESTIMATED ENERGY COSTS**'][i] = 0.0
            else:
                graph['ESTIMATED ENERGY COSTS**'][i] = float(graph['ESTIMATED ENERGY COSTS**'][i])

            # print(graph['ESTIMATED ENERGY USAGE*'][i])
            
            # process the estimated energy usage data
            if '–' in graph['ESTIMATED ENERGY USAGE*'][i]:
                # print("I come into the if statment")
                tmp = graph['ESTIMATED ENERGY USAGE*'][i].split('–')
                graph['ESTIMATED ENERGY USAGE*'][i] = (float(tmp[0]) + float(tmp[1])) / 2
            else:
                graph['ESTIMATED ENERGY USAGE*'][i] = float(graph['ESTIMATED ENERGY USAGE*'][i])
    
        # print(graph['ESTIMATED ENERGY USAGE*'])
        #transfer the data 

        return graph

    def read_user_option(self, graph):
        #initialize some of the variable used in this method
        cat1 = graph['CATEGORY1'][0] +" " +graph['CATEGORY2'][0]
        cate_min = ''
        price_min = 9999999
        total_save = 0
        detail = {}

        print("\n\nWelcome to the demo part for calculating your energy consumption and saving money!\nYou can enter q to exit this flow")
        for i in range(len(graph['CATEGORY1'])):
            # if categories change, then print all the options and let the user choose from them
            if str(graph['CATEGORY1'][i]) +" " + str(graph['CATEGORY2'][i]) != cat1:
                print("\n**Category: ", cat1)
                # print(detail)
                for j in range(len(detail)):
                    print(j+1, '. ', list(detail)[j])
                choice = input("please Enter your choice or leave it blank: ")
                if choice == 'q':
                    break
                if choice != '':
                    choice = int(choice) - 1
                    if list(detail.values())[choice][0]*list(detail.values())[choice][1] != price_min:
                        print("Your choice is ", list(detail.keys())[choice], ", this would cost ", list(detail.values())[choice][0]*list(detail.values())[choice][1], 
                        "dollar per hour\n", "If you choose ", cate_min, ", you will save", list(detail.values())[choice][0]*list(detail.values())[choice][1]-price_min,
                        "dollar per hour!")
                        total_save += list(detail.values())[choice][0]*list(detail.values())[choice][1]-price_min
                    else:
                        print("Congratulations! You have made the most energy saving choice!")
                    print("In this suggestion flow you have saved ", total_save, "dollars per hour!!")
                    #demo the least one
                else:
                    print("Please choose ", cate_min, " as your choice! This choice saves energy and will cost you ", price_min, " dollar per hour!\nOr you choosing not to involve this category")
                detail = {}
                detail[graph['DETAIL'][i]] = [graph['ESTIMATED ENERGY USAGE*'][i], graph['ESTIMATED ENERGY COSTS**'][i]]
                cate_min = graph['DETAIL'][i]
                price_min = graph['ESTIMATED ENERGY USAGE*'][i] * graph['ESTIMATED ENERGY COSTS**'][i]
                cat1 = str(graph['CATEGORY1'][i]) + " " + str(graph['CATEGORY2'][i])
            else:
                detail[graph['DETAIL'][i]] = [graph['ESTIMATED ENERGY USAGE*'][i], graph['ESTIMATED ENERGY COSTS**'][i]]
                if graph['ESTIMATED ENERGY USAGE*'][i] * graph['ESTIMATED ENERGY COSTS**'][i] < price_min:
                    cate_min = graph['DETAIL'][i]
                    price_min = graph['ESTIMATED ENERGY USAGE*'][i] * graph['ESTIMATED ENERGY COSTS**'][i] 
        print("\nYou have saved ", total_save, "dollars per hour in the whole program flow!!!")
        print("\nThank you for using demo program to reduce your energy costs and your money!")
        #return total_save

    def co2_emi_capita(self, filename, sheetname):
        df1 = pd.read_excel(open(filename, 'rb'), sheet_name=sheetname) 
        df_USA_individual = df1.iloc[21232:21451]
        df_USA_individual.plot(x="Year", y='Per capita CO2 emissions')
        plt.show()



if __name__ == '__main__':
    # you can enter the file location in this part to initial the class
    filename = r'D:\project_agg\21S_DFP_project\Big_project\Project_Prototype_DFP_group12.xlsx' 
    sheetname_emission_per_capita = r'Worldbank CO2-emissions_capita'
    sheetname_interactive = r'Appliance Energy Use_Clean'
    signal = True
    print("Scrape is starting, it may take a few seconds to finish")
    web = webscrape.ncdc_pre() #initial a new class from webscrape
    df = web.clean_data(web.scrape())


    # project begin
    print("\nWelcome to the demo project which could help you be a more environmental friendly person!")
    while signal:
        print("\nPlease make your choice:\n1. Display the Global Land and Sea Yearly Temperature Anomalies Chart\n2. Display the Top Ten Hottest Years on Record Chart\n3. Display CO2 Emissions per Capita Chart\n4. Suggestions for Your Energy Clean Choice\n5. Quit")
        choice = input("Your choice is: ")
        if choice == '1':
            web.draw_temp_anomly(df)
        elif choice == '2':
            web.draw_top10(df)
        elif choice == '3':
            suggestion().co2_emi_capita(filename, sheetname_emission_per_capita)
        elif choice == '4':
            graph = suggestion().readdata(filename, sheetname_interactive)
            #print(graph)
            suggestion().read_user_option(graph)
        elif choice == '5':
            signal = False
            print("Thank you for using the demo project!!")
        else:
            print("\nYour input is invalid! Please re-try!")
    

