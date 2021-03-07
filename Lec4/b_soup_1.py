#Author: Team 2, Haonan Di, Xiaoting Wang
#author andrew id: hdi, xiaotinw
from urllib.request import urlopen  # b_soup_1.py
from bs4 import BeautifulSoup
import re 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd 


# part a)
def generate_data():
    '''can pass some parameter, for example year, in this HW just a function to fetch the data'''

    # change to year 2020, just change the index is fine
    html = urlopen('https://www.treasury.gov/resource-center/'
                'data-chart-center/interest-rates/Pages/'
                'TextView.aspx?data=yieldYear&year=2020')

    bsyc = BeautifulSoup(html.read(), "lxml")

    # only one class="t-chart" table, so add that
    # to findAll as a dictionary attribute
    tc_table_list = bsyc.findAll('table',
                        { "class" : "t-chart" } )

    # only 1 t-chart table, so grab it
    tc_table = tc_table_list[0]

    # we have found the table data!
    # just get the contents of each cell

    # every 13 cells will be in a loop
    daily_yield_curves = []
    mode13 = 0
    tmp = []
    for c in tc_table.children:
        for r in c.children:
            if mode13 % 13 == 0:
                daily_yield_curves += [tmp]
                tmp = [r.contents[0]]
                mode13 += 1
            else:
                mode13 += 1
                try:
                    tmp += [float(r.contents[0])]
                except:
                    tmp += [r.contents[0]]
            #print(r.contents)

    daily_yield_curves.pop(0)
    # print(daily_yield_curves)
    return daily_yield_curves


# part b)
def draw_3D_plot(daily_yield_curves):
    X = []
    Y = []
    Z = []
    tmpx = 0  # start from day 0
    for lines in daily_yield_curves[1:]:
        tmp_len = len(lines)
        X += [[tmpx] * (tmp_len-1)]
        Y += [[1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]]
        Z += [lines[1:]]
        tmpx += 1
    
    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    # print(len(X[0]))
    # print(len(Y[0]))
    # print(len(Z[0]))
    # have checked X, Y, Z. for (x, y) in Z
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection = '3d')
    surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased=False)
    
    plt.show()
    
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1, projection = '3d')
    wir = ax2.plot_wireframe(X, Y, Z, rstride = 3, cstride = 3)
    plt.show()


# part c
def pandas_analysis(daily_yield_curves):
    

    yield_curve_df = pd.DataFrame(daily_yield_curves[1:], columns=daily_yield_curves[0])
    yield_curve_df.set_index(['Date'], inplace=True)
    
    
    yield_curve_df.plot()
    plt.title("Interest Rate Time Series, 2020")
    plt.show()

    # transpose the yield_curve_df and plot again
    # yield_curve_df.T.plot()
    # plt.show()

    tmp_len = len(yield_curve_df.index)
    tmp_lst = [i*20 for i in range(tmp_len//20 + 1)]
    by_day_yield_curve_df = yield_curve_df.iloc[tmp_lst, ].T 
    mon = [1, 2, 3, 6, 12, 24, 36, 60, 84, 120, 240, 360]
    by_day_yield_curve_df.index = mon  # set the correct index for the monthly curve
    by_day_yield_curve_df.plot()
    plt.title("2020 Yield Curves, 20 Day Intervals")
    plt.show()




daily_yield_curves = generate_data()

draw_3D_plot(daily_yield_curves)
pandas_analysis(daily_yield_curves)
