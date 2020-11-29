import pandas as pd
import numpy as np
#import seaborn as sb
#import plotly as ptly
import matplotlib.pyplot as plt

class dataVisualization:
    def __init__(self):
        self.pyplot = plt
        #self.seaborn = sb
        #self.plotly = ptly

        #color list
        self.colorlist=['r','g','b','c','m','y','k','w']

    def barchart(self,x_label,y_label,x_data,y_data,title):
        fig = self.pyplot.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.bar(x_data,y_data)
        self.pyplot.show()

    def barchartWithMultiColumn(self,data):
        '''
        Note: 1. This function can plot upto 8 columns with unique color value including white(#fff)
              2. Function enhancement required, columns are overlapping
              3. data parameter must be a multidimensional list
        '''
        X = np.arange(4)
        fig = self.pyplot.figure()
        ax = fig.add_axes([0,0,1,1])
        length=len(data)
        for inc in range(length):
            ax.bar(X + 0.25*inc,data[inc],color=self.colorlist[inc],width=0.25)
        self.pyplot.show()

    def barchartWithThreshold(self,threshold,values,x_label,y_label):
        '''
        Note: values parameter must be a numpy array
        '''
        x = range(len(values))
        # split it up
        above_threshold = np.maximum(values - threshold, 0)
        below_threshold = np.minimum(values, threshold)
        # and plot it
        fig, ax = self.pyplot.subplots()
        ax.bar(x, below_threshold, 0.35, color="g")
        ax.bar(x, above_threshold, 0.35, color="r",
                bottom=below_threshold)
        #set labels
        ax.set_xlabel=x_label
        ax.set_ylabel=y_label
        # horizontal line indicating the threshold
        ax.plot([0., 4.5], [threshold, threshold], "k--")
        self.pyplot.show()

    def piechart(self,labels,data,title):
        fig = self.pyplot.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.axis('equal')
        dataList = data
        labelsList = labels 
        ax.pie(dataList, labels = labelsList,autopct='%1.2f%%')
        self.pyplot.show()

    def heatmap(self,dataframe):
        labels=[]
        for col in dataframe.columns:
            labels.append(col)

        corelationMatrix=dataframe.corr()
        fig, ax = self.pyplot.subplots()
        ax.set_xticks(np.arange(dataframe.shape[0]))
        ax.set_yticks(np.arange(dataframe.shape[0]))
        ax.set_xticklabels(labels)
        ax.set_yticklabels(labels)
        im = ax.imshow(corelationMatrix)
        self.pyplot.setp(ax.get_xticklabels(), rotation=45, ha="right",
                rotation_mode="anchor")
        # Loop over data dimensions and create text annotations.
        for i in range(dataframe.shape[0]):
            for j in range(dataframe.shape[0]):
                text = ax.text(j, i, dataframe.iloc[i, j],
                            ha="center", va="center", color="w")

        self.pyplot.show()