import cx_Oracle as db
import pandas as pd

#importing database credentials
import os
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

class menuSource:
    def __init__(self):
        #class member variable initialization
        self.tableName = "mc_donalds_menu"
        self.dbUserName = os.environ.get('DATABASE_USERNAME')
        self.dbUserPassword = os.environ.get('DATABASE_PASSWORD')
        self.connectionString = self.dbUserName+'/'+self.dbUserPassword+'@localhost'
        #db connection 
        self.con = db.connect(self.connectionString)
        self.cursor=self.con.cursor()
        #create dataframe
        self.baseQuery="select * from mc_donalds_menu"
        self.df=pd.read_sql(self.baseQuery,self.con)
   
    #member fucntions for dataset meta data
    def getColumnNames(self):
        headerList=[]
        for col in self.df.columns:
            headerList.append(col)
        return headerList
        #print(headerList)
    
    def getSizeOfDataSet(self):
        return self.df.size
    
    def getDataSetInfo(self):
        return self.df.info()
    
    def getDataSetShape(self):
        map={"rows":self.df.shape[0],"columns":self.df.shape[1]}
        return map

    #member functions for data access
    def getAllDataFromCursor(self):
        self.cursor.execute(self.baseQuery)
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

    def getDistinctValuesFromColumn(self):
        query="select distinct category from mc_donalds_menu"
        df = pd.read_sql(query,self.con)
        return df

    def getItemByCategory(self,category):
        query="select ITEM from mc_donalds_menu where CATEGORY='"+category+"'"
        df = pd.read_sql(query,self.con)
        return df

class safeValueSource:
    def __init__(self):
        #class member variable initialization
        self.tableName = "nutritional_safe_values"
        self.dbUserName = os.environ.get('DATABASE_USERNAME')
        self.dbUserPassword = os.environ.get('DATABASE_PASSWORD')
        self.connectionString = self.dbUserName+'/'+self.dbUserPassword+'@localhost'
        #db connection 
        self.con = db.connect(self.connectionString)
        self.cursor=self.con.cursor()
        #create dataframe
        self.baseQuery="select * from nutrition_safe_values"
        self.df=pd.read_sql(self.baseQuery,self.con)

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
    def getSafeValueByNutirentFromCursor(self,nutrients):
        condition=" where"
        key=" nutrient="
        s1=""
        for i in range(len(nutrients)-1):
            s1+=key+"'"+str(nutrients[i])+"'"+" OR "
        s1+=key+"'"+str(nutrients[len(nutrients)-1])+"'"

        query= self.baseQuery+condition+s1
        self.cursor.execute(query)
        return self.cursor

    def getAllSafeValuesFromCursor(self):
        self.cursor.execute(self.baseQuery)
        return self.cursor

    def getSafeValueByNutirentFromDataFrame(self,nutrients):
        condition=" where"
        key=" nutrient="
        s1=""
        for i in range(len(nutrients)-1):
            s1+=key+"'"+str(nutrients[i])+"'"+" OR "
        s1+=key+"'"+str(nutrients[len(nutrients)-1])+"'"

        query= self.baseQuery+condition+s1
        df = pd.read_sql(query,self.con)
        return df

    def getAllSafeValuesFromDataFrame(self):
        return self.df

class userManagement:
    def __init__(self):
        #class member variable initialization
        self.tableName = "user_login_data"
        self.dbUserName = os.environ.get('DATABASE_USERNAME')
        self.dbUserPassword = os.environ.get('DATABASE_PASSWORD')
        self.connectionString = self.dbUserName+'/'+self.dbUserPassword+'@localhost'
        #db connection 
        self.con = db.connect(self.connectionString)
        self.cursor=self.con.cursor()
        #create dataframe
        self.baseQuery="select * from user_login_data"

    def signup(self,username,password):
        query="insert into user_login_data values("+"'"+username+"','"+password+"')"
        self.cursor.execute(query)
        self.cursor.execute('commit')
        print("data inserted successfully")

    def login(self,username,password):
        query=self.baseQuery+" where username="+"'"+username+"' and password="+"'"+password+"'"
        #print(query)
        self.cursor.execute(query)
        list=[]
        for row in self.cursor:
            list.append(row)
        if len(list)!=0:
            return True
        else:
            return False
