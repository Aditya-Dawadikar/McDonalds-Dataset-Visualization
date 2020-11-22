import cx_Oracle as db
import pandas as pd

class menuSource:
    def __init__(self,dbUserName,dbPassword):
        #class member variable initialization
        self.tableName = "mc_donalds_menu"
        self.dbUserName = dbUserName
        self.dbUserPassword = dbPassword
        self.connectionString = self.dbUserName+'/'+self.dbUserPassword+'@localhost'
        #db connection 
        self.con = db.connect(self.connectionString)
        self.cursor=self.con.cursor()
        #create dataframe
        baseQuery="select * from mc_donalds_menu"
        self.df=pd.read_sql(baseQuery,self.con)
   
    #member fucntions for dataset meta data
    def getColumnNames(self):
        headerList=[]
        for col in self.df.columns:
            headerList.append(col)
        return headerList
    
    def getSizeOfDataSet(self):
        return self.df.size
    
    def getDataSetInfo(self):
        return self.df.info()
    
    def getDataSetShape(self):
        map={"rows":self.df.shape[0],"columns":self.df.shape[1]}
        return map

    #member functions for data access
    def getAllDataFromCursor(self):
        query="select * from mc_donalds_menu"
        self.cursor.execute(query)
        return self.cursor
    
    def getAllDataFromDataFrame(self):
        return self.df
    
    def selectQueryFromCursor(self,columnList):
        #create string that contains column names for select clause
        queryCols=""
        for i in range(len(columnList)-1):
            queryCols+=columnList[i]
            queryCols+=','
        queryCols+=columnList[len(columnList)-1]
        #print(queryCols)
        #compose query
        query = "select "+queryCols+" from mc_donalds_menu"
        #return cursor object
        self.cursor.execute(query)
        for row in self.cursor:
            print(row)
        return self.cursor
    
    def selectQueryFromDataFrame(self,columnList):
        #create string that contains column names for select clause
        queryCols=""
        for i in range(len(columnList)-1):
            queryCols+=columnList[i]
            queryCols+=','
        queryCols+=columnList[len(columnList)-1]
        #print(queryCols)
        #compose query
        query = "select "+queryCols+" from mc_donalds_menu"
        #return dataframe
        df = pd.read_sql(query,self.con)
        return df
    
    def selectQueryWithConstraintsFromCursor(self,columnList,constraintString):
        #create string that contains column names for select clause
        queryCols=""
        for i in range(len(columnList)-1):
            queryCols+=columnList[i]
            queryCols+=','
        queryCols+=columnList[len(columnList)-1]
        #print(queryCols)
        #compose query
        query = "select "+queryCols+" from mc_donalds_menu "+constraintString
        #return cursor object
        self.cursor.execute(query)
        for row in self.cursor:
            print(row)
        return self.cursor
    
    def selectQueryWithConstraintsFromDataFrame(self,columnList,constraintString):
        #create string that contains column names for select clause
        queryCols=""
        for i in range(len(columnList)-1):
            queryCols+=columnList[i]
            queryCols+=','
        queryCols+=columnList[len(columnList)-1]
        #print(queryCols)
        #compose query
        query = "select "+queryCols+" from mc_donalds_menu "+constraintString
        #return dataframe
        df = pd.read_sql(query,self.con)
        return df