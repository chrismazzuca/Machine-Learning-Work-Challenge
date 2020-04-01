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


# Create and save a bar chart
def saveBarChart(data, file, filePath):
    # Get the participation, employment, and unemployment rates from the data
    participation_rate = data.loc['Participation rate', '19-Feb'].values
    employment_rate = data.loc['Employment rate', '19-Feb'].values
    unemployment_rate = data.loc['Unemployment rate', '19-Feb'].values

    # Plot a bar chart of the data
    labels = ['Both (15+)', 'Both (15-24)', 'Men (25+)', 'Women (25+)']
    x = np.arange(len(labels))
    fig, ax = plt.subplots()
    ax.bar(x - 0.25, participation_rate, 0.25, label='Participation Rate')
    ax.bar(x, employment_rate, 0.25, label='Employment Rate')
    ax.bar(x + 0.25, unemployment_rate, 0.25, label='Unemployment Rate')

    # Add labels and save the chart
    ax.set_ylabel('Percentage')
    ax.set_title('Employment rates ({})'.format(file[:-4]))
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    plt.show()
    ax.figure.savefig(filePath)


############## Visualize Employment Data by industry ##############
# subdir = "Employment Data/By industry/"
# for _, _, files in os.walk(subdir):
#     for file in files:
#         # Read each file, and create a pie chart
#         data = pd.read_csv(subdir + file, index_col=0)
#         savePieChart(data, file, 'Plots/By industry/' + file[:-4])
###################################################################


########## Visualize Employment Data by age group and sex ##########
# subdir = "Employment Data/By age group and sex/"
# for _, _, files in os.walk(subdir):
#     for file in files:
#         # Read each file, and create a pie chart
#         data = pd.read_csv(subdir + file, index_col=0)
#         saveBarChart(data, file, 'Plots/By age group and sex/' + file[:-4])
###################################################################