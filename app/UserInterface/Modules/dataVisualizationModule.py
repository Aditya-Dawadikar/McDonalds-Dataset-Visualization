import pandas as pd
import numpy as np
#import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


class dataVisualization:
    def __init__(self):
        self.pyplot = plt
        #self.seaborn = sb
        #self.plotly = ptly
        self.dataSet=pd.read_csv('menu.csv')
        self.df=pd.DataFrame(self.dataSet)

        #color list
        self.colorlist=['r','g','b','c','m','y','k','w']

    #def barchart(self,x_label,y_label,x_data,y_data,title):
    def barchart(self,col_name):
        #col_name is a list
        plot_list=['Category']
        for i in col_name:
            plot_list.append(i)
        minerals = self.df[plot_list]

        minerals_group = minerals.groupby('Category')
        
        category_totals = minerals_group.mean()
        title = "nutrient in each Category in Menu Data-set of McDonald's Menu"
        x_label = "Food Categories in Menu"
        y_label = "Range"

        my_plot = category_totals.plot(kind='bar',figsize=(10, 5),fontsize=12 )
        plt.setp(my_plot.get_xticklabels(), rotation=30)
        my_plot.set_title(title, fontsize=20)
        my_plot.set_xlabel(x_label, fontsize=10)
        my_plot.set_ylabel(y_label, fontsize=15)
        plt.show()

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

    def swarmplot(self,Category_Min):
        Category_List=self.df['Category'].unique()
        dataframe=[]
        for i in Category_Min:
            l=self.df[i].tolist()
            dataframe.append(l)

        fig = go.Figure()

        for i in range(len(dataframe)):
            fig.add_trace(go.Box(y=dataframe[i],opacity=1,fillcolor="rgba(0,0,0,0)",boxpoints="all",jitter=0.8,line={"width": 0},pointpos=0,name=Category_List[i]))

        fig.update_layout(showlegend=False)
        fig.show()

    def heatMap(self,category):
        #category is a string
        subData=[]
        dataList=[]
        it1=0
        flag=0
        for i in self.df['Category']:
            it2=it1
            if(category==self.df['Category'].iloc[it1]):
                for j in self.df['Category']:
                    #print(self.df.iloc[it1])
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

        print(corrMat)
        #fig = px.imshow(z,labels=dict(x="Nutrient", y="Nutrient", color="Productivity"),x=cols,y=cols)
        #fig.show()

        fig = ff.create_annotated_heatmap(z, x=cols, y=cols)
        for i in range(len(fig.layout.annotations)):
            fig.layout.annotations[i].font.size = 8
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
        labels = [
        'Calories',
        'Fat',
        'Saturated Fat',
        'Trans Fat',
        'Cholesterol',
        'Sodium',
        'Carbohydrates',
        'Dietary Fiber',
        'Sugars',
        'Protein']

        maxValues=[120,17.5,5,2,0.3,2.3,325,30,1.5,1]
        minValues=[80,3,1.5,0,0,0,225,25,0.3,0.8]

        dataList=[]

        it1=0
        flag=0
        for i in self.df['Category']:
            it2=it1
            if(category==self.df['Category'].iloc[it1]):
                for j in self.df['Item']:
                    if(food==self.df['Item'].iloc[it2]):
                        dataList=self.df.iloc[it1].tolist()
                        flag=1
                    break
                    it2+=1
            if flag==1:
                break
            it1+=1

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
        # Change the bar mode
        fig.update_layout(barmode='group',title_text='Safe value comparison for '+food+" per 100 gram of serving")
        fig.update_layout()
        fig.show()
