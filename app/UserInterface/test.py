import Modules.dataVisualizationModule as dvm

obj=dvm.dataVisualization()

x_data=[10,20,8,70]
y_data=[10,12,9,11]
Category_Min = ['Calories', 'Total Fat', 'Cholesterol','Sodium', 'Sugars', 'Carbohydrates']
obj.heatMap()