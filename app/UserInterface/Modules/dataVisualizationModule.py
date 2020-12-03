import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

class dataVisualization:
    def __init__(self):
        self.dataSet=pd.read_csv('menu.csv')
        self.df=pd.DataFrame(self.dataSet)

    def swarmplot(self,category,Nutrient_List):
        dataframe=[]
        
        for i in Nutrient_List:
            l=[]
            for it in range(259):
                if(self.df['Category'].iloc[it]==category):
                    l.append(self.df[i].iloc[it])
            dataframe.append(l)
        fig = go.Figure()

        for i in range(len(dataframe)):
            fig.add_trace(go.Box(y=dataframe[i],opacity=1,fillcolor="rgba(0,0,0,0)",boxpoints="all",jitter=0.8,line={"width": 0},pointpos=0,name=Nutrient_List[i]))

        fig.update_layout()
        fig.show()
        
    def heatMap(self,category):
        subData=[]
        dataList=[]
        it1=0
        flag=0
        for i in self.df['Category']:
            it2=it1
            if(category==self.df['Category'].iloc[it1]):
                for j in self.df['Category']:
                    if(category==self.df['Category'].iloc[it2]):
                        dataList=self.df.iloc[it1].tolist()
                        subData.append(dataList[3:24])
                    else:
                        flag=1
                    break
                    it2+=1
            if flag==1:
                break
            it1+=1

        cols=['Calories',
        'Calories from Fat',
        'Total Fat',
        'Total Fat (% Daily Value)',
        'Saturated Fat',
        'Saturated Fat (% Daily Value)',
        'Trans Fat',
        'Cholesterol',
        'Cholesterol (% Daily Value)',
        'Sodium',
        'Sodium (% Daily Value)',
        'Carbohydrates',
        'Carbohydrates (% Daily Value)',
        'Dietary Fiber',
        'Dietary Fiber (% Daily Value)',
        'Sugars',
        'Protein',
        'Vitamin A (% Daily Value)',
        'Vitamin C (% Daily Value)',
        'Calcium (% Daily Value)',
        'Iron (% Daily Value)']

        df1= pd.DataFrame(subData,columns=cols)
        corrMat=df1.corr()
        z=[]

        for i in range(corrMat.shape[1]):
            corrMat.iloc[i]=corrMat.iloc[i].round(decimals=2)

        for i in range(corrMat.shape[0]):
            l=corrMat.iloc[i].tolist()
            z.append(l)

        fig = ff.create_annotated_heatmap(z, x=cols, y=cols)
        for i in range(len(fig.layout.annotations)):
            fig.layout.annotations[i].font.size = 8
        fig.update_layout(title_text='heat map for '+category)
        fig.show()

    def donut(self,category,food):
        labels = [
        'Saturated Fat',
        'Trans Fat',
        'Cholesterol',
        'Sodium',
        'Carbohydrates',
        'Dietary Fiber',
        'Sugars',
        'Protein']

        values = []
        dataList=[]

        it1=0
        flag=0
        for i in self.df['Category']:
            it2=it1
            if(category==self.df['Category'].iloc[it1]):
                for j in self.df['Item']:
                    #print(self.df.iloc[it1])
                    if(food==self.df['Item'].iloc[it2]):
                        dataList=self.df.iloc[it1].tolist()
                        flag=1
                    break
                    it2+=1
            if flag==1:
                break
            it1+=1

        values.append(dataList[7])
        values.append(dataList[9])
        values.append(dataList[10]*0.001)
        values.append(dataList[12]*0.000001)
        values.append(dataList[14])
        values.append(dataList[16])
        values.append(dataList[18])
        values.append(dataList[19])

        # Use `hole` to create a donut-like pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_layout(
        title_text="Nutritional Constituents in "+food,
        # Add annotations in the center of the donut pies.
        annotations=[dict(text=food, x=0.5, y=0.5, font_size=20, showarrow=False)])
        fig.show()

    def safeValueComparison(self,category,food):
        labels = ['Calories','Fat','Saturated Fat','Trans Fat','Cholesterol','Sodium','Carbohydrates','Dietary Fiber','Sugars','Protein']
        maxValues=[120,17.5,5,2,0.3,2.3,325,30,1.5,1]
        minValues=[80,3,1.5,0,0,0,225,25,0.3,0.8]

        dataList=[]

        for i in range(259):
            if(food==self.df['Item'].iloc[i]):
                dataList=self.df.iloc[i].tolist()
                break

        values=[]
        values.append(dataList[3])
        values.append(dataList[5])
        values.append(dataList[7])
        values.append(dataList[9])
        values.append(dataList[10]*0.001)
        values.append(dataList[12]*0.000001)
        values.append(dataList[14])
        values.append(dataList[16])
        values.append(dataList[18])
        values.append(dataList[19])

        fig = go.Figure(data=[
            go.Bar(name='Min requirement per 100g serving', x=labels, y=minValues),
            go.Bar(name='Actual Value per 100g serving', x=labels, y=values),
            go.Bar(name='Max requirement per 100g serving', x=labels, y=maxValues)
        ])
        fig.update_layout(barmode='group',title_text='Safe value comparison for '+food+" per 100 gram of serving")
        fig.update_layout()
        fig.show()

    # bar graph for multifood category, single nutrient
    def bar1(self,food_category,column):
        values=[]
        print(len(food_category))
        
        for category in food_category:
            start=0; 
            for i in range(self.df.shape[0]):
                if(category==self.df['Category'].iloc[i]):
                    start=i
                    break
            l=[]
            it=start
            while (self.df['Category'].iloc[it]==category and it<259):
                l.append(self.df[column].iloc[it])
                it+=1        
            values.append(stat.mean(l))
           
        fig = go.Figure([go.Bar(x=food_category, y=values)])
        fig.update_layout(title_text="Avegrage "+column+" in particular categories")
        fig.show()
        
    #bar graph for metal,fat,vitamin comparison for particular item
    def bar2(self,food,status):
        #must pass name of food and status code 1,2 or 3 depending on the type of graph required
        nutrient=[]
        values=[]

        '''
        status map:
            1: metal 2: fats 3: vitamin

        index map:
            metals: 
                sodium: 13 iron:23 calcium:22

            fats:
                total: 5 saturated: 7 trans:9

            vitamin
                vitamin A: 20 vitamin C: 21 
        '''

        row=[]
        for i in range(self.df.shape[0]):
            if(food==self.df['Item'].iloc[i]):
                row=self.df.iloc[i].tolist()
                break

        if(status==1):
            #metals
            nutrient.append(row[13])
            nutrient.append(row[22])
            nutrient.append(row[23])
            values.append('Sodium % Daily Value')
            values.append('Calcium % Daily Value')
            values.append('Iron % Daily Value')
        
        elif(status==2):
            #fats
            nutrient.append(row[5])
            nutrient.append(row[7])
            nutrient.append(row[9])
            values.append('Total Fat per 100g')
            values.append('Saturated Fat per 100g')
            values.append('Transfat per 100g')

        elif(status==3):
            #vitamin
            nutrient.append(row[20])
            nutrient.append(row[21])
            values.append('Vitamin A % Daily Value')
            values.append('Vitamin C % Daily Value')


        fig = go.Figure([go.Bar(x=values, y=nutrient)])
        fig.update_layout(title_text="nutrient comparison for "+food)
        fig.show()

    #bar graph for single nutrient and multiple categories
    def bar3(self,food):
        labels = ['Calories','Fat','Saturated Fat','Trans Fat','Cholesterol','Sodium','Carbohydrates','Dietary Fiber','Sugars','Protein']
        dataList=[]

        for i in range(259):
            if(food==self.df['Item'].iloc[i]):
                dataList=self.df.iloc[i].tolist()
                break

        values=[]
        values.append(dataList[3])
        values.append(dataList[5])
        values.append(dataList[7])
        values.append(dataList[9])
        values.append(dataList[10]*0.001)
        values.append(dataList[12]*0.000001)
        values.append(dataList[14])
        values.append(dataList[16])
        values.append(dataList[18])
        values.append(dataList[19])

        fig = go.Figure(data=[go.Bar(name='Actual Value per 100g serving', x=labels, y=values)])
        fig.update_layout(barmode='group',title_text='Nutrient Comparison for '+food+" per 100 gram of serving")
        fig.show()