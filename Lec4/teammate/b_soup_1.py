# Authors: Xiaoting Wang
# File name for homework4: b_soup_1.py
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def retrieve_data(year):
    html = urlopen('https://www.treasury.gov/resource-center/'
               'data-chart-center/interest-rates/Pages/'
               'TextView.aspx?data=yieldYear&year=' + str(year))

    bsyc = BeautifulSoup(html.read(), "lxml")

    tc_table_list = bsyc.findAll('table', { "class" : "t-chart" } )
    tc_table = tc_table_list[0]

    daily_yield_curves = []
    for tr in tc_table.select('tr'):
        line = []
        for c in tr.children:
            line.append(c.contents[0])
        daily_yield_curves.append(line)

    for r in range(1,len(daily_yield_curves)):
        for c in range(1,len(daily_yield_curves[0])):
            daily_yield_curves[r][c] = float(daily_yield_curves[r][c])
    
    return daily_yield_curves

def write_data(daily_yield_curves, filename):
    # Make the data neat so as to write in a file
    with open(filename, 'wt', encoding='utf-8') as fout:
        output = ''
        output += '{:<12s}'.format(daily_yield_curves[0][0])
        for i in range(1,13):
            output += '{:<8s}'.format(daily_yield_curves[0][i])
        output += '\n'
        fout.write(output)
    
        for row in range(1,len(daily_yield_curves)):
            output = ''
            output += '{:<12s}'.format(daily_yield_curves[row][0])
            for i in range(1,13):
                output += '{:<8.2f}'.format(daily_yield_curves[row][i])
            output += '\n'
            fout.write(output)

def plot_surf_wireframe(daily_yield_curves):
    date_map = dict(zip(daily_yield_curves[0][1:],
                    [int(x.split(' ')[0]) if 'mo' in x else int(x.split(' ')[0]) * (len(daily_yield_curves[0]) - 1) for x in daily_yield_curves[0][1:]]))
    rowsnum = len(daily_yield_curves) - 1
    months = np.array([[date_map[x] for x in daily_yield_curves[0][1:]] for i in range(rowsnum)])
    data = np.array(daily_yield_curves)
    dates = np.array([[i]*len(months[0]) for i in range(len(data[1:,0]))])
    interests = data[1:, 1:]
    interests = interests.astype('float')

    fig = plt.figure(figsize=(8,10))
    ax = fig.add_subplot(2, 1, 1, projection='3d')
    # Firts Plot
    surf = ax.plot_surface(dates, months, interests, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
    ax.set_ylim((0,350))
    ax.set_zlim(0, 4.0)
    ax.zaxis.set_major_locator(LinearLocator(9))
    ax.set_xlabel('trading days since 01/02/20')
    ax.set_ylabel('months to maturity')
    ax.set_zlabel('rate')

    fig.colorbar(surf, shrink=0.5, aspect=10)

    #Second Plot
    ax1 = fig.add_subplot(2, 1, 2, projection='3d')

    ax1.set_ylim((0,350))
    ax1.set_zlim(0, 4.0)
    ax1.zaxis.set_major_locator(LinearLocator(9))
    ax1.set_xlabel('trading days since 01/02/20')
    ax1.set_ylabel('months to maturity')
    ax1.set_zlabel('rate')

    wireframe = ax1.plot_wireframe(dates, months, interests)
    plt.show()

def yield_curve_plot(daily_yield_curves):
    data = np.array(daily_yield_curves)
    yield_curve_df = pd.DataFrame(data[1:,1:], index=data[1:,0], columns=data[0,1:])
    yield_curve_df = yield_curve_df.astype('float')
    yield_curve_df.plot(figsize=(10,8), title='Interest Rate Time Series, 2020')
    plt.show()

    dates = list(yield_curve_df.index)
    by_day_yield_curve_df = yield_curve_df.loc[[dates[i] for i in range(len(dates)) if i % 20 == 0]]

    date_map = dict(zip(daily_yield_curves[0][1:],
                    [int(x.split(' ')[0]) if 'mo' in x else int(x.split(' ')[0])*12 for x in daily_yield_curves[0][1:]]))
    by_day_yield_curve_df.rename(columns=date_map, inplace=True)
    by_day_yield_curve_df.transpose().plot(figsize=(10,8), title='2020 Yield Curves, 20 Day Intervals')
    plt.show()



def main():
    print(retrieve_data(2019))
    data_2020 = retrieve_data(2020)
    write_data(data_2020, 'daily_yield_curves.txt')
    plot_surf_wireframe(data_2020)
    yield_curve_plot(data_2020)


if __name__ == '__main__':
	main()