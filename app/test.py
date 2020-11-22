#importing app modules
import Modules.databaseModule as dbm
import Modules.dataVisualizationModule as dvm 
import Modules.statisticsModule as stm 

#importing database credentials
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

#establish connection with database
db = dbm.menuSource(os.environ.get('DATABASE_USERNAME'),os.environ.get('DATABASE_USERNAME'))

barchartPlotter = dvm.plainPlot()

x_label="language"
y_label="range"
x_data=['C', 'C++', 'Java', 'Python', 'PHP']
y_data=[23,17,35,29,12]
title="language vs student count"

barchartPlotter.barchart(x_label,y_label,x_data,y_data,title)