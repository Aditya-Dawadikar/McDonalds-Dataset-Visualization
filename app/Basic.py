import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
import pandas as pd
import Modules.dataVisualizationModule as dvm 
import Modules.statisticsModule as sm
import sys
from Data import dataList
class Ui_MainWindow(object):
    def __init__(self):
        self.state=0
        
#system functions
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.model = QStandardItemModel()

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(210, 0, 341, 81))
        self.titleLabel.setStyleSheet("color:rgb(255, 0, 0)")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")

        self.categoryRadio = QtWidgets.QRadioButton(self.centralwidget) # category with nutrtion radio button
        self.categoryRadio.setGeometry(QtCore.QRect(30, 119, 160, 21))
        self.categoryRadio.setObjectName("categoryRadio")
        self.categoryRadio.toggled.connect(self.manageCategoryWithNutrition)
        self.categoryRadio.toggled.connect(self.radioToggle)

        self.foodItemRadio = QtWidgets.QRadioButton(self.centralwidget) # Food item radio button
        self.foodItemRadio.setGeometry(QtCore.QRect(200, 120, 95, 20))
        self.foodItemRadio.setObjectName("foodItemRadio")
        self.foodItemRadio.toggled.connect(self.manageFoodItem)
        self.foodItemRadio.toggled.connect(self.radioToggle)

        self.analyzeLabel = QtWidgets.QLabel(self.centralwidget)  # "what do u want to analyze" label
        self.analyzeLabel.setGeometry(QtCore.QRect(10, 70, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.analyzeLabel.setFont(font)
        self.analyzeLabel.setObjectName("analyzeLabel")

        self.nutritionRadio = QtWidgets.QRadioButton(self.centralwidget) #Comparison of Nutrition radio button
        self.nutritionRadio.setGeometry(QtCore.QRect(300, 116, 181, 31))
        self.nutritionRadio.setObjectName("nutritionRadio")
        self.nutritionRadio.toggled.connect(self.manageComparisonOfNutrition)
        self.nutritionRadio.toggled.connect(self.radioToggle)

        self.categoryCombo = QtWidgets.QComboBox(self.centralwidget) # Category combo box
        self.categoryCombo.setGeometry(QtCore.QRect(60, 380, 91, 31))
        self.categoryCombo.setObjectName("categoryCombo")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.addItem("")
        self.categoryCombo.setModel(self.model)
        self.categoryCombo.hide()

        self.categoryLabel = QtWidgets.QLabel(self.centralwidget)   #Category Label
        self.categoryLabel.setGeometry(QtCore.QRect(10, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("categoryLabel")

        self.nutritionLabel = QtWidgets.QLabel(self.centralwidget) #nutrtion label
        self.nutritionLabel.setGeometry(QtCore.QRect(300, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nutritionLabel.setFont(font)
        self.nutritionLabel.setObjectName("nutritionLabel")

        self.showButton = QtWidgets.QPushButton(self.centralwidget) #show visualization button
        self.showButton.setGeometry(QtCore.QRect(280, 420, 111, 31))
        self.showButton.setObjectName("showButton")
        self.showButton.clicked.connect(self.show)
        self.showButton.setStyleSheet("border:2px solid black;\n"
"border-radius:\"20px\";\n"
"font-weight: lighter;")

        self.safetyRadio = QtWidgets.QRadioButton(self.centralwidget) #safty values radio button
        self.safetyRadio.setGeometry(QtCore.QRect(470, 116, 211, 31))
        self.safetyRadio.setObjectName("safetyRadio")
        self.safetyRadio.toggled.connect(self.manageSafetyValues)
        self.safetyRadio.toggled.connect(self.radioToggle)

        self.newCategoryRadio_2 = QtWidgets.QRadioButton(self.centralwidget) #For category 
        self.newCategoryRadio_2.setGeometry(QtCore.QRect(690, 121, 82, 17))
        self.newCategoryRadio_2.setObjectName("newCategoryRadio_2")
        self.newCategoryRadio_2.toggled.connect(self.manageCategory)
        self.newCategoryRadio_2.toggled.connect(self.radioToggle)


        self.nutritionList = QtWidgets.QListWidget(self.centralwidget) #Nutrition list
        self.nutritionList.setGeometry(QtCore.QRect(380, 180, 256, 106))
        self.nutritionList.setObjectName("nutritionList")
        self.nutritionList.setSelectionMode(2)

        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.nutritionList.addItem(item)

        self.categoryList = QtWidgets.QListWidget(self.centralwidget) #category list
        self.categoryList.setGeometry(QtCore.QRect(100, 180, 181, 106))
        self.categoryList.setObjectName("categoryList")
        self.categoryList.setSelectionMode(2)

        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.categoryList.addItem(item)

        self.foodItemCombo = QtWidgets.QComboBox(self.centralwidget)  #Food item combo box
        self.foodItemCombo.setGeometry(QtCore.QRect(200, 380, 121, 22))
        self.foodItemCombo.setObjectName("foodItemCombo")
        self.foodItemCombo.setModel(self.model)
        self.foodItemCombo.hide()

        self.foodItemLabel = QtWidgets.QLabel(self.centralwidget)
        self.foodItemLabel.setGeometry(QtCore.QRect(370, 370, 81, 31))
        self.foodItemLabel.hide()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.foodItemLabel.setFont(font)
        self.foodItemLabel.setObjectName("foodItemLabel")

        self.graphLabel = QtWidgets.QLabel(self.centralwidget)  # "which graph" label
        self.graphLabel.setGeometry(QtCore.QRect(10, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.graphLabel.setFont(font)
        self.graphLabel.setObjectName("graphLabel")

        self.pieRadio = QtWidgets.QRadioButton(self.centralwidget) #Pie chart radio button
        self.pieRadio.setGeometry(QtCore.QRect(30, 350, 81, 21))
        self.pieRadio.setObjectName("pieRadio")

        self.barRadio = QtWidgets.QRadioButton(self.centralwidget) #Bar graph radio button
        self.barRadio.setGeometry(QtCore.QRect(30, 380, 81, 21))
        self.barRadio.setObjectName("barRadio")

        self.scatterRadio = QtWidgets.QRadioButton(self.centralwidget) #Scatter radio button
        self.scatterRadio.setGeometry(QtCore.QRect(180, 350, 250, 21))
        self.scatterRadio.setObjectName("scatterRadio")

        self.nutritionOptionCombo = QtWidgets.QComboBox(self.centralwidget) # for option of nutrition comparison
        self.nutritionOptionCombo.setGeometry(QtCore.QRect(530, 500, 141, 22))
        self.nutritionOptionCombo.setObjectName("nutritionOptionCombo")
        self.nutritionOptionCombo.addItem("")
        self.nutritionOptionCombo.addItem("")
        self.nutritionOptionCombo.addItem("")
        self.nutritionOptionCombo.hide()

        self.summaryRadio = QtWidgets.QRadioButton(self.centralwidget) #For summary Radio Button
        self.summaryRadio.setGeometry(QtCore.QRect(785, 120, 200, 17))
        self.summaryRadio.setObjectName("summaryRadio")
        self.summaryRadio.toggled.connect(self.manageSummary)
        self.summaryRadio.toggled.connect(self.radioToggle)

        self.summaryLabel = QtWidgets.QLabel(self.centralwidget)  #For Sumary Label
        self.summaryLabel.setGeometry(QtCore.QRect(480, 400, 300, 13))
        self.summaryLabel.setObjectName("summaryLabel")
        self.summaryLabel.hide()

        self.columnSummaryCombo = QtWidgets.QComboBox(self.centralwidget)
        self.columnSummaryCombo.setGeometry(QtCore.QRect(560, 400, 69, 22))
        self.columnSummaryCombo.setObjectName("columnSummaryCombo")
        self.columnSummaryCombo.hide()
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")
        self.columnSummaryCombo.addItem("")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 91, 51))
        self.label.setStyleSheet("image: url(assets/mcDonald1.jpeg);\n"
"border-radius: 15px")
        self.label.setText("")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        for k,v in dataList.items():            #Logic for dynamic combobox values 
            category=QStandardItem(k)
            self.model.appendRow(category)
            for item in v:
                fooditem=QStandardItem(item)
                category.appendRow(fooditem)

        self.categoryCombo.currentIndexChanged.connect(self.updatefoodItemCombo) # for updation of index
        self.updatefoodItemCombo(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", " McDonald\'s Food Ananlysis"))
        self.categoryRadio.setText(_translate("MainWindow", "Category with Nutrition"))
        self.foodItemRadio.setText(_translate("MainWindow", "Food Items"))
        self.analyzeLabel.setText(_translate("MainWindow", "What do you want to analyze?"))
        self.nutritionRadio.setText(_translate("MainWindow", "Comparison of Nutritions"))
        self.categoryCombo.setItemText(0, _translate("MainWindow", "Breakfast"))
        self.categoryCombo.setItemText(1, _translate("MainWindow", "Beek&Pork"))
        self.categoryCombo.setItemText(2, _translate("MainWindow", "Chicken&Fish"))
        self.categoryCombo.setItemText(3, _translate("MainWindow", "Salads"))
        self.categoryCombo.setItemText(4, _translate("MainWindow", "Snacks & Sides"))
        self.categoryCombo.setItemText(5, _translate("MainWindow", "Desserts"))
        self.categoryCombo.setItemText(6, _translate("MainWindow", "Beverages"))
        self.categoryCombo.setItemText(7, _translate("MainWindow", "Coffee & Tea"))
        self.categoryCombo.setItemText(8, _translate("MainWindow", "Smoothies & Shakes"))
        self.categoryLabel.setText(_translate("MainWindow", "Category :"))
        self.nutritionLabel.setText(_translate("MainWindow", "Nutritions :"))
        self.showButton.setText(_translate("MainWindow", "Show Visualization"))
        self.safetyRadio.setText(_translate("MainWindow", "Comparison with Safety Values"))
        __sortingEnabled = self.nutritionList.isSortingEnabled()
        self.nutritionList.setSortingEnabled(False)
        item = self.nutritionList.item(0)
        item.setText(_translate("MainWindow", "Calories"))
        item = self.nutritionList.item(1)
        item.setText(_translate("MainWindow", "Total Fat (% Daily Value)"))
        item = self.nutritionList.item(2)
        item.setText(_translate("MainWindow", "Cholesterol (% Daily Value)"))
        item = self.nutritionList.item(3)
        item.setText(_translate("MainWindow", "Sodium (% Daily Value)"))
        item = self.nutritionList.item(4)
        item.setText(_translate("MainWindow", "Carbohydrates (% Daily Value)"))
        item = self.nutritionList.item(5)
        item.setText(_translate("MainWindow", "Dietary Fiber (% Daily Value)"))
        item = self.nutritionList.item(6)
        item.setText(_translate("MainWindow", "Sugars"))
        item = self.nutritionList.item(7)
        item.setText(_translate("MainWindow", "Protein"))
        item = self.nutritionList.item(8)
        item.setText(_translate("MainWindow", "Vitamin A (% Daily Value)"))
        item = self.nutritionList.item(9)
        item.setText(_translate("MainWindow", "Vitamin C (% Daily Value)"))
        item = self.nutritionList.item(10)
        item.setText(_translate("MainWindow", "Calcium (% Daily Value)"))
        item = self.nutritionList.item(11)
        item.setText(_translate("MainWindow", "Iron (% Daily Value)"))
        self.nutritionList.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.categoryList.isSortingEnabled()
        self.categoryList.setSortingEnabled(False)
        item = self.categoryList.item(0)
        item.setText(_translate("MainWindow", "Breakfast"))
        item = self.categoryList.item(1)
        item.setText(_translate("MainWindow", "Beef & Pork"))
        item = self.categoryList.item(2)
        item.setText(_translate("MainWindow", "Chicken & Fish"))
        item = self.categoryList.item(3)
        item.setText(_translate("MainWindow", "Salads"))
        item = self.categoryList.item(4)
        item.setText(_translate("MainWindow", "Snacks & Sides"))
        item = self.categoryList.item(5)
        item.setText(_translate("MainWindow", "Desserts"))
        item = self.categoryList.item(6)
        item.setText(_translate("MainWindow", "Beverages"))
        item = self.categoryList.item(7)
        item.setText(_translate("MainWindow", "Coffee & Tea"))
        item = self.categoryList.item(8)
        item.setText(_translate("MainWindow", "Smoothies & Shakes"))
        self.categoryList.setSortingEnabled(__sortingEnabled)
        self.foodItemLabel.setText(_translate("MainWindow", "Food Item :"))
        self.foodItemLabel.setText(_translate("MainWindow", "Food Item :"))
        self.graphLabel.setText(_translate("MainWindow", "Select the type of graph :"))
        self.pieRadio.setText(_translate("MainWindow", "Pie chart"))
        self.barRadio.setText(_translate("MainWindow", "Bar Graph"))
        self.scatterRadio.setText(_translate("MainWindow", "Swarm Plot(single category, multiple nutrients)"))
        self.newCategoryRadio_2.setText(_translate("MainWindow", "Category"))
        self.nutritionOptionCombo.setItemText(0, _translate("MainWindow", "Metal"))
        self.nutritionOptionCombo.setItemText(1, _translate("MainWindow", "Fat"))
        self.nutritionOptionCombo.setItemText(2, _translate("MainWindow", "Vitamin"))
        self.summaryRadio.setText(_translate("MainWindow", "Summary of Nutrient"))
        self.summaryLabel.setText(_translate("MainWindow", "TextLabel"))
        self.columnSummaryCombo.setItemText(0, _translate("MainWindow", "Calories"))
        self.columnSummaryCombo.setItemText(1, _translate("MainWindow", "Total Fat"))
        self.columnSummaryCombo.setItemText(2, _translate("MainWindow", "Cholesterol"))
        self.columnSummaryCombo.setItemText(3, _translate("MainWindow", "Sodium"))
        self.columnSummaryCombo.setItemText(4, _translate("MainWindow", "Carbohydrates"))
        self.columnSummaryCombo.setItemText(5, _translate("MainWindow", "Dietary Fiber"))
        self.columnSummaryCombo.setItemText(6, _translate("MainWindow", "Sugars"))
        self.columnSummaryCombo.setItemText(7, _translate("MainWindow", "Protein"))
        self.columnSummaryCombo.setItemText(8, _translate("MainWindow", "Vitamin A (% Daily Value)"))
        self.columnSummaryCombo.setItemText(9, _translate("MainWindow", "Vitamin C (% Daily Value)"))
        self.columnSummaryCombo.setItemText(10, _translate("MainWindow", "Calcium (% Daily Value)"))
        self.columnSummaryCombo.setItemText(11, _translate("MainWindow", "Iron (% Daily Value)"))

#UI management functions
    def updatefoodItemCombo(self,index):
        ind=self.model.index(index,0,self.categoryCombo.rootModelIndex())
        self.foodItemCombo.setRootModelIndex(ind)
        self.foodItemCombo.setCurrentIndex(0)

    def manageCategoryWithNutrition(self,selected):  # to display the necessary GUI for Category with nutrtion wise analysis
        if selected:
            self.categoryCombo.hide()
            self.foodItemCombo.hide()
            self.foodItemLabel.hide()
            self.nutritionOptionCombo.hide()
            self.pieRadio.hide()
            self.summaryLabel.hide()
            self.columnSummaryCombo.hide()

            self.categoryLabel.setGeometry(QtCore.QRect(10, 180, 81, 31))
            self.categoryLabel.show()
            self.categoryList.setGeometry(QtCore.QRect(100, 180, 181, 106))
            self.categoryList.setSelectionMode(2)
            self.categoryList.show()
            self.nutritionLabel.setGeometry(QtCore.QRect(300, 180, 91, 31))
            self.nutritionLabel.show()
            self.nutritionList.setGeometry(QtCore.QRect(380, 180, 256, 106))
            self.nutritionList.setSelectionMode(2)
            self.nutritionList.show()
            self.graphLabel.setText("Select the type of graph :")
            self.graphLabel.show()
            self.barRadio.setGeometry(QtCore.QRect(30, 350, 500, 21))
            self.barRadio.setText("Bar chart(Multiple category, single nutrient)")
            self.barRadio.show()
            self.scatterRadio.setGeometry(QtCore.QRect(30, 380, 400, 21))
            self.scatterRadio.show()
            self.showButton.setText("Show Visualization")

    def manageFoodItem(self,selected):  # to display the necessary GUI for Food item wise analysis
        if selected:
            self.categoryList.hide()
            self.nutritionOptionCombo.hide()
            self.scatterRadio.hide()
            self.nutritionLabel.hide()
            self.nutritionList.hide()
            self.summaryLabel.hide()
            self.columnSummaryCombo.hide()

            self.categoryLabel.setGeometry(QtCore.QRect(10, 180, 81, 31))
            self.categoryLabel.show()
            self.categoryCombo.setGeometry(QtCore.QRect(90, 185, 150, 31))
            self.categoryCombo.show()
            self.foodItemLabel.setGeometry(QtCore.QRect(270, 180, 81, 31))
            self.foodItemLabel.show()
            self.foodItemCombo.setGeometry(QtCore.QRect(360, 185, 350, 31))
            self.foodItemCombo.show()
            self.graphLabel.setText("Select the type of graph :")
            self.graphLabel.show()
            self.pieRadio.setText("Donut ")
            self.pieRadio.show()
            self.barRadio.setGeometry(QtCore.QRect(30, 380, 81, 21))
            self.barRadio.setText("Bar chart")
            self.barRadio.show()
            self.showButton.setText("Show Visualization")

    def manageComparisonOfNutrition(self,selected):  #Display necessary GUI for Comaprison of nutritions
         if selected:
            self.categoryList.hide()
            self.nutritionList.hide()
            self.pieRadio.hide()
            self.barRadio.hide()
            self.scatterRadio.hide()
            self.summaryLabel.hide()
            self.columnSummaryCombo.hide()

            self.categoryLabel.setGeometry(QtCore.QRect(10, 180, 81, 31))
            self.categoryLabel.show()
            self.categoryCombo.setGeometry(QtCore.QRect(90, 185, 150, 31))
            self.categoryCombo.show()
            self.foodItemLabel.setGeometry(QtCore.QRect(270, 180, 81, 31))
            self.foodItemLabel.show()
            self.foodItemCombo.setGeometry(QtCore.QRect(360, 185, 350, 31))
            self.foodItemCombo.show()
            self.nutritionLabel.setGeometry(QtCore.QRect(760, 180, 91, 31))
            self.nutritionLabel.show()
            self.nutritionOptionCombo.setGeometry(QtCore.QRect(851, 185, 100, 31))
            self.nutritionOptionCombo.show()
            self.graphLabel.setText("By Deafult it will generate Bar Graph:")
            self.graphLabel.show()
            self.showButton.setText("Show Visualization")
          
    def manageSafetyValues(self,selected):    #Display GUI for safety values
        if selected:
            self.categoryList.hide()
            self.nutritionOptionCombo.hide()
            self.nutritionLabel.hide()
            self.nutritionList.hide()
            self.pieRadio.hide()
            self.barRadio.hide()
            self.scatterRadio.hide()
            self.summaryLabel.hide()
            self.columnSummaryCombo.hide()

            self.categoryLabel.setGeometry(QtCore.QRect(10, 180, 81, 31))
            self.categoryLabel.show()
            self.categoryCombo.setGeometry(QtCore.QRect(90, 185, 150, 31))
            self.categoryCombo.show()
            self.foodItemLabel.setGeometry(QtCore.QRect(270, 180, 81, 31))
            self.foodItemLabel.show()
            self.foodItemCombo.setGeometry(QtCore.QRect(360, 185, 350, 31))
            self.foodItemCombo.show()
            self.graphLabel.setText("By default it will generate a bar graph")
            self.graphLabel.adjustSize()
            self.graphLabel.show()
            self.showButton.setText("Show Visualization")
            
    def manageCategory(self,selected): #Display GUI for category 
        if selected:
            self.nutritionLabel.hide()
            self.nutritionList.hide()
            self.pieRadio.hide()
            self.scatterRadio.hide()
            self.barRadio.hide()
            self.nutritionOptionCombo.hide()
            self.foodItemLabel.hide()
            self.foodItemCombo.hide()
            self.categoryCombo.hide()
            self.summaryLabel.hide()
            self.columnSummaryCombo.hide()

            self.categoryList.setGeometry(QtCore.QRect(100, 180, 181, 106))
            self.categoryList.show()
            self.categoryList.setSelectionMode(1)
            self.categoryLabel.show()
            self.graphLabel.setText("By Default it will generate Heatmap")
            self.graphLabel.adjustSize()
            self.showButton.setText("Show Visualization")
            self.graphLabel.show()

    def manageSummary(self,selected):
        if selected:
            self.categoryLabel.hide()
            self.categoryList.hide()
            self.categoryCombo.hide()
            self.nutritionLabel.hide()
            self.nutritionList.hide()
            self.nutritionOptionCombo.hide()
            self.foodItemLabel.hide()
            self.foodItemCombo.hide()
            self.graphLabel.hide()
            self.pieRadio.hide()
            self.barRadio.hide()
            self.scatterRadio.hide()
            
            self.summaryLabel.setText("Select Column")
            self.summaryLabel.setGeometry(QtCore.QRect(290, 135, 300, 206))
            self.summaryLabel.show()
            self.columnSummaryCombo.setGeometry(QtCore.QRect(390, 230, 180, 22))
            self.columnSummaryCombo.show()
            self.showButton.setText("View Summary")

#data management functions

    graphChoice = 1
    def show(self):
        graphChoice = 1
        #For selection of graph radio buttons
        if self.pieRadio.isChecked()==True:
            graphChoice=1
        elif self.scatterRadio.isChecked()==True:
            graphChoice=2
        elif self.barRadio.isChecked()==True:
            graphChoice=3

        self.visualization(self.state ,graphChoice)

    def radioToggle(self):
        #For selection of main radio buttons
        if self.categoryRadio.isChecked()==True:
           self.state=1
        elif self.foodItemRadio.isChecked()==True:
            self.state=2
        elif self.nutritionRadio.isChecked()==True:
            self.state=3
        elif self.safetyRadio.isChecked()==True:
            self.state=4
        elif self.newCategoryRadio_2.isChecked()==True:
            self.state=5
        elif self.summaryRadio.isChecked()==True:
            self.state=6


    def visualization(self,state,graphChoice):
        if(state==1):  # For category with Nutrition
            items=self.categoryList.selectedItems()

            # #select the categories
            categorySelect=[]
            for i in range(len(items)):
                categorySelect.append(str(self.categoryList.selectedItems()[i].text()))

            nutritionItems=self.nutritionList.selectedItems()
            nutritionSelect=[]
            for i in range(len(nutritionItems)):
                nutritionSelect.append(str(self.nutritionList.selectedItems()[i].text()))
            #select nutrition
            nutritent=self.nutritionList.selectedItems()
            
            # #select the categories
            nutrientSelect=[]
            for i in range(len(nutritent)):
                nutrientSelect.append(str(self.nutritionList.selectedItems()[i].text()))

            obj=dvm.dataVisualization()
            
            #selected graph function calls
            if graphChoice == 2:
                obj.swarmplot(categorySelect[0],nutrientSelect)
            elif graphChoice == 3:
                obj.bar1(categorySelect,str(nutrientSelect[0]))

        elif(state==2):  # For Food Item 
            #Select category
            category= self.categoryCombo.currentText()
            #Select food item 
            foodItem= self.foodItemCombo.currentText()

            items=self.nutritionList.selectedItems()
            #select the nutritions
            nutritionSelect=[]
            for i in range(len(items)):
                nutritionSelect.append(str(self.nutritionList.selectedItems()[i].text()))

            obj=dvm.dataVisualization()

            if graphChoice == 1:
                obj.donut(category,foodItem)
            elif graphChoice == 3:
                 obj.bar3(foodItem)

            
        elif(state==3):   # For comparison of nutrtion
            foodItem = self.foodItemCombo.currentText()
            status = self.nutritionOptionCombo.currentIndex()
            obj=dvm.dataVisualization()
            obj.bar2(foodItem,status+1)

        elif(state==4):     # For comparison with saftey values
            #Select food item 
            category = self.categoryCombo.currentText()
            foodItem= self.foodItemCombo.currentText()
            obj = dvm.dataVisualization()
            obj.safeValueComparison(category,foodItem)

        elif (state==5):
            category = self.categoryList.selectedIndexes()[0]
            obj=dvm.dataVisualization()
            obj.heatMap(str(category.data()))

        elif (state==6):
            colName=self.columnSummaryCombo.currentText()
            obj=sm.statisticsModule()
            result=obj.getSummary(colName)
            cnt=str(result['row count'])
            minResult=str(result['minimum'])
            maxResult=str(result['maximum'])
            meanResult=str(result['mean'])
            modeResult=str(result['mode'])
            medianResult=str(result['median'])
            varienceResult=str(result['variance'])
            stdResult=str(result['standard deviation'])
            
            resultString="Count: "+cnt+"\n\nMinimum: "+minResult+"\n\nMaximum: "+maxResult+"\n\nMean: "+meanResult+"\n\nMode: "+modeResult+"\n\nMedian: "+medianResult+"\n\nVariance: "+varienceResult+"\n\nStandard Deviation: "+stdResult
            
            self.columnSummaryCombo.hide()
            self.summaryLabel.setGeometry(QtCore.QRect(290, 170, 300, 206))
            self.summaryLabel.setText(resultString)


        return 

class UiCaller:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    
#main function
uiObj=UiCaller()