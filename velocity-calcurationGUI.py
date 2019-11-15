import pandas as pd
import matplotlib.pyplot as plt
import os

def draw_line_graph_from_csv(file_name, x_axis, y_axes=None):
    df = pd.read_csv(file_name)
    #filter = [x_axis] + y_axes

    #title = os.path.basename(file_name)
    #df[filter].plot(x=x_axis, title=title, grid=True, rot=10, figsize=(6, 4))


    fig = plt.figure()
    fig.subplots_adjust(bottom=0.2)
    fig.subplots_adjust(right=0.85)
    fig.subplots_adjust(left=0.15)

    ax1 = fig.add_subplot(1,1,1)
    ax2 = ax1.twinx()
    ax3 = ax1.twinx()

    ax1.set_xlabel('time',fontsize=18)
    ax1.set_ylabel('frequency',fontsize = 18, color = 'red')
    ax2.set_ylabel('phase',fontsize = 18, color = 'green')
    ax3.set_ylabel('adcvalue',fontsize = 18, color = 'blue')

    rspine = ax3.spines['right']
    rspine.set_position(('axes', 1.20))

    ax1.plot(df['frequency'],color = 'red',label = "frequency")
    ax2.plot(df['phase'],color = 'green',label = "phase")
    ax3.plot(df['adcvalue'],color = 'blue',label = "adcvalue")

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    h3, l3 = ax3.get_legend_handles_labels()
    ax1.legend(h1 + h2 +h3, l1 + l2 +l3 ,loc='upper right')

    plt.show()

draw_line_graph_from_csv('1911141707Freq-Velocity_Table_USM1-goodresult.csv', 'time', ['phase', 'frequency', 'adcvalue'])