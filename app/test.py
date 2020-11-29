#importing app modules
#import Modules.databaseModule as dbm
#import Modules.dataVisualizationModule as dvm 
#import Modules.statisticsModule as stm 
#import numpy as np
#import pandas as pd

#importing database credentials
#import os
#from dotenv import load_dotenv,find_dotenv

#load_dotenv(find_dotenv())

#establish connection with database
#menudb = dbm.menuSource()
#safeValuedb = dbm.safeValueSource()
#umdb=dbm.userManagement()

import UserInterface.Basic 

Basic.visualization()