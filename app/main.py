#importing app modules
import Modules.databaseModule as dbm
import Modules.dataVisualizationModule as dvm 
import Modules.statisticsModule as stm 

#importing database credentials
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

#establish connection with database
db = dbm(os.environ.get('DATABASE_USERNAME'),os.environ.get('DATABASE_USERNAME'))