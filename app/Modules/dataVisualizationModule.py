import pandas as pd
#import seaborn as sb
#import plotly as ptly
import matplotlib.pyplot as plt

class dataVisualization:
    def __init__(self):
        self.pyplot = plt
        #self.seaborn = sb
        #self.plotly = ptly

class plainPlot(dataVisualization):
    def __init__(self):
        dataVisualization.__init__(self)
        #simple bar graphs
    
    def barchart(self,x_label,y_label,x_data,y_data,title):
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.bar(x_data,y_data)
        plt.show()
        
class plainComparisonPlot(dataVisualization):
    def __init__(self):
        dataVisualization.__init__(self)
        #bar graphs for comparison
        
class comparisonWithStandardPlot(dataVisualization):
    def __init__(self):
        dataVisualization.__init__(self)
        #bar graphs for comparison with standard safe value
        
class constituentComparisonPlot(dataVisualization):
    def __init__(self):
        dataVisualization.__init__(self)
        #pie charts