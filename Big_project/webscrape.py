# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:16:14 2021

@author: KZF552
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
sns.set_theme(style="whitegrid")
import pandas as pd

class ncdc_pre:
    def __init__(self):
        return

    def scrape(self):
        
        options = Options()
        options.add_argument("headless")
        driver = webdriver.Chrome(chrome_options=options)

        driver.get("https://www.ncdc.noaa.gov/cag/global/time-series")
        time.sleep(1)

        '''
        # write out all HTML for review and submnission
        with open('page.html', 'w') as f:
            f.write(driver.page_source)
        '''

        # Find the table
        table = driver.find_element_by_xpath("//table[@class='tablesorter tablesorter-default']")

        years = []
        # Collect the years
        for row in table.find_elements_by_xpath(".//tr"):
            year = ([td.text for td in row.find_elements_by_xpath(".//td[@class='date']")])
            years += year


        values = []    
        #Collect the temps
        for row in table.find_elements_by_xpath(".//tr"):
            value = ([td.text for td in row.find_elements_by_xpath(".//td[@class='value']")])
            values += value

        #print(values)
        driver.close()

        merged_list = [(years[i], values[i]) for i in range(0, len(years))] 
        #print(merged_list)
        return merged_list


        # write out all data for submnission
        '''
        with open('chart_data.txt', 'w') as f:
            f.write(str(merged_list))
        '''

        '''
        https://www.ncei.noaa.gov/news/global-climate-202101
        The January 2021 global land and ocean surface temperature was the seventh highest 
        in the 142-year record at 1.44°F (0.80°C) above the 
        20th-century average of 53.6°F (12.0°C). 

        January 2021 marked the 45th consecutive January and 
        the 433rd consecutive month with temperatures, at least nominally, 
        above the 20th-century average.

        '''
        '''
        Chart 1:  Yearly Trend
        '''

    def clean_data(self, merged_list):
        # create DataFrame using data 
        sorted_merged_data = sorted(merged_list)
        df = pd.DataFrame(sorted_merged_data, columns =['Year', 'Temp Anamoly']) 
        # remove celsius symbol and letter
        df['Temp Anamoly'] = df['Temp Anamoly'].map(lambda x: str(x)[:-2])
        # convert temp to float and year to int
        df["Year"] = pd.to_numeric(df["Year"], downcast='integer')
        df["Temp Anamoly"] = pd.to_numeric(df["Temp Anamoly"], downcast="float")
        # Add derived field to identify Years >= 2015
        df['gt 2014'] = ['Yes' if x >= 2015 else 'No' for x in df['Year']]

        return df 
    
    def draw_temp_anomly(self, df):
         
        # Yearly Chart
        plt.plot(df['Year'], df['Temp Anamoly']) 
        plt.xlabel("")  # add X-axis label 
        plt.ylabel("Temp Anamoly")  # add Y-axis label 
        plt.title("Land/Sea Temperature Anamoly by Year")  # add title  
        plt.axhline(linewidth=2, color='r')  #horizontal line 
        plt.figtext(0.14, 0.01, "Source: https://www.ncdc.noaa.gov/cag/global/time-series", ha="left", fontsize=8)
        plt.show() 

    def draw_top10(self, df):
        # Top 10 Hottest Years Chart
        x = df.sort_values('Temp Anamoly',ascending = False).head(10)
        # sort again for chart
        x = x.sort_values('Temp Anamoly',ascending = True)
        # Create chart
        x.plot('Year','Temp Anamoly',color=['b', 'r', 'b', 'b', 'r', 'b', 'r', 'r', 'r', 'r'],kind='bar', legend=False)
        plt.xlabel("")  # add X-axis label 
        plt.tick_params(labelsize=10, rotation = 0)
        plt.ylabel("Temp Anamoly", fontsize=10)  # add Y-axis label 
        plt.grid(False)
        plt.title("Six of the Ten Hottest Years on Record are in the Last Six Years", fontsize=10)  # add title  
        plt.figtext(0.14, 0.01, "Source: https://www.ncdc.noaa.gov/cag/global/time-series", ha="left", fontsize=8)
        plt.show() 


