import pandas as pd
import seaborn as sb
import plotly as ptly
import matplotlib.pyplot as plt
#from databaseModule import menuSource

class dataVisualization:
    def __init__(self):
        self.pyplot = plt
        self.seaborn = sb
        self.plotly = ptly
        #self.datasource = ds

class plainPlot(dataVisualization):
    def __init__(self):
        dataVisualization.__init__(self)
        #simple bar graphs
        
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