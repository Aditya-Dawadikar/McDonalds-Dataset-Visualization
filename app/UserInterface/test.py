import Modules.dataVisualizationModule as dvm
import numpy as np
obj=dvm.dataVisualization()

x_data=[10,20,8,70]
y_data=[10,12,9,11]
Nutrient = ['Calories', 'Total Fat', 'Cholesterol','Sodium', 'Sugars', 'Carbohydrates']

l=np.array([1,4,2,5,2,6,1,7,4,7])
x_labels=[1,4,2,5,2,6,1,7,4,7]
y_labels=[1,4,2,5,2,6,1,7,4,7]
obj.swarmplot(Nutrient)
