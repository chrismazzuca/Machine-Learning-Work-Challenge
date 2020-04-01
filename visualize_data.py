import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create and save a pie chart
def savePieChart(data, file, filePath):
    # Get the most recent information (February 19th)
    data.drop(data.index[0], inplace=True)
    labels = data.index.values
    pie_sizes = data.loc[:, '19-Feb'].values

    # Sort the data, and remove smaller industries
    labels = labels[pie_sizes.argsort()]
    pie_sizes = pie_sizes[pie_sizes.argsort()]
    labels = labels[pie_sizes > 0.04 * pie_sizes.sum()]
    other_sizes = pie_sizes.sum() - pie_sizes[pie_sizes > 0.04 * pie_sizes.sum()].sum()
    pie_sizes = pie_sizes[pie_sizes > 0.04 * pie_sizes.sum()]
    labels = np.append(labels, 'Other')
    pie_sizes = np.append(pie_sizes, other_sizes)

    # Create a pie chart to visualize the distribution, and save it
    _, fig = plt.subplots()
    fig.pie(pie_sizes, autopct='%1.1f%%', startangle=320)
    fig.axis('equal')
    plt.title('Employment by industry ({})'.format(file[:-4]))
    fig.legend(labels=labels, loc='upper left', prop={'size': 6})
    plt.show()
    fig.figure.savefig(filePath)


############## Visualize Employment Data by industry ##############
subdir = "Employment Data/By industry/"
for _, _, files in os.walk(subdir):
    for file in files:
        # Read each file, and create a pie chart
        data = pd.read_csv(subdir + file, index_col=0)
        savePieChart(data, file, 'Plots/By industry/' + file[:-4])
###################################################################