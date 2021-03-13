import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt 


df1 = pd.read_excel(open('Project_Prototype_DFP_group12.xlsx', 'rb'), sheet_name='Worldbank CO2-emissions_capita') 
df_USA_individual = df1.iloc[21232:21451]
df_USA_individual.plot(x="Year", y='Per capita CO2 emissions')

plt.show()