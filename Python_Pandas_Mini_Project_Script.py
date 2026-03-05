import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset

data = pd.read_csv('c:/Users/HP/OneDrive/Documents/SWAROOP DOCUMENTS/Agileology_Docs/Cafe_Sales.csv')

# Overview of the dataset:

print(data.info())  #Summary of the dataset

print(data.describe()) #Statistical summary of numerical columns


#1) identify and handle missing values in key fields:

data.iloc[0:,1:].fillna(np.nan, inplace=True)

print(data.head(100).to_string())


# #2) Convert data types to appropriate formats (e.g., dates, numeric types):

print(data.dtypes)

data["Transaction Date"] = pd.to_datetime(data["Transaction Date"], errors='coerce')

data["Quantity"] = pd.to_numeric(data["Quantity"],errors= "coerce")

data["Price Per Unit"] = pd.to_numeric(data["Price Per Unit"],errors = "coerce")

data["Total Spent"] = pd.to_numeric(data["Total Spent"],errors= "coerce")

print(data.dtypes)


# #3) correct the incorrect or inconsistent data entries(entries UNKNOWN,ERROR):

# #A) Correcting UNKNOWN entries: 

print(data.head(100).to_string())

mod1 = data["Item"].mode()[0]

data["Item"].replace("UNKNOWN",mod1, inplace=True)   



mean1 = data["Quantity"].mean()

data["Quantity"].replace("UNKNOWN", mean1, inplace=True)


mean2 = data["Price Per Unit"].mean()

data["Price Per Unit"].replace("UNKNOWN", mean2, inplace=True)


mean3 = data["Total Spent"].mean()

data["Total Spent"].replace("UNKNOWN", mean3, inplace=True)


mod2   = data["Payment Method"].mode()[0]

data["Payment Method"].replace("UNKNOWN", mod2, inplace=True)


mod3 = data["Location"].mode()[0]   

data["Location"].replace("UNKNOWN", mod3, inplace=True) 


mean4 = data["Transaction Date"].mean()

data["Transaction Date"].replace("UNKNOWN", mean4, inplace=True)


# #B) Correcting ERROR entries:

data["Item"].replace("ERROR",mod1, inplace=True)   

med1 = data["Quantity"].median()

data["Quantity"].replace("ERROR",med1, inplace=True)   


med2 = data["Price Per Unit"].median()

data["Price Per Unit"].replace("ERROR",med2, inplace=True)   


med3 = data["Total Spent"].median()

data["Total Spent"].replace("ERROR",med3, inplace=True)   


data["Payment Method"].replace("ERROR",mod2, inplace=True)   


data["Location"].replace("ERROR",mod3, inplace=True)   

med4 = data["Transaction Date"].median()

data["Transaction Date"].replace("ERROR",med4, inplace=True)
 
print(data.head(100).to_string())


#4 Replacing any remaining NaN values with appropriate statistics:

data["Item"].replace(np.nan,mod1, inplace=True)

data["Quantity"].replace(np.nan,mean1, inplace=True)

data["Price Per Unit"].replace(np.nan,mean2, inplace=True)

data["Total Spent"].replace(np.nan,mean3, inplace=True)

data["Payment Method"].replace(np.nan,mod2, inplace=True)

data["Location"].replace(np.nan,mod3, inplace=True)

data["Transaction Date"].replace(np.nan,mean4, inplace=True)

print(data.head(100).to_string())



#5) Removing duplicate records from the dataset:

print(data.duplicated().to_string())

data.drop_duplicates(inplace=True)

print(data.duplicated().to_string())



#6) Correlation analysis between numerical fields:

print(data.corr(numeric_only=True))


#7) Visualizations to illustrate key findings from the data:

data.plot(kind='hist', x='Quantity', y='Total Spent', title='Quantity vs Total Spent')
plt.xlabel('Quantity')
plt.ylabel('Total Spent')
plt.show()


data.plot(kind='hist', x='Price Per Unit', y='Total Spent', title='Price Per Unit vs Total Spent')
plt.xlabel('Price Per Unit')
plt.ylabel('Total Spent')
plt.show()

