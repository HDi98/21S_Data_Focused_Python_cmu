import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 
import re 


class suggestion:
    filename = ''
    sheetname = ''

    def __init__(self):
        return 
    
    def setroot(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def readdata(self):
        '''clean data for this part should be a xlsx file so we must specify the filename and sheetname'''
        try:
            graph = pd.read_excel(filename, sheet_name=sheetname)
        except:
            print("filename or sheetname is wrong, Please check your input")
            return 
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

    def read_user_option(self):
        graph = self.readdata()

        return 




if __name__ == '__main__':
    filename = r'D:\project_agg\21S_DFP_project\Big_project\Project_Prototype_DFP_group12.xlsx'
    sheetname = r'Appliance Energy Use_Clean'
    graph = suggestion().readdata()
    print(graph)