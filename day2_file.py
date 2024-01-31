# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:53:35 2024

@author: sikha
"""

import pandas as pd 
df = pd.read_csv("country_data_index.csv")

import pandas as pd 
file = pd.read_csv("iris.csv")


"""
EXTRACT
"""

"""
Absolute path 
- full path/location 
-e.g C:/Users/sikha/css2024_day2/iris.csv

Relative path 
- depends where you are
- e.g iris.csv

"""

file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

file = pd.read_csv(url)

#Adding columns to the data
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
file = pd.read_csv(url, header=None, names= column_names)

"""
Diffrent file types (used relative paths; can use abosulte)
"""
#Text file with semi-colon
file = pd.read_csv("Geospatial Data.txt", sep=';')

#Excel
file = pd.read_excel("residentdoctors.xlsx")
# for a specific sheet: sheet = "sheet1"


#Json 
file = pd.read_json("student_data.json")
print(file)
 

url = "https://github.com/Asabele240701/css4_day02/blob/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
df = pd.read_csv(url)
print(df.info())
print(df.describe())



"""
TRANSFORM 
"""
#Index columns 

df = pd.read_csv("country_data_index.csv")

df = pd.read_csv("country_data_index.csv",index_col=0)

#Skip rows

df = pd.read_csv("insurance_data.csv")
df = pd.read_csv("insurance_data.csv",skiprows=5)

# Column headings 
df = pd.read_csv("patient_data.csv")
column_names = ["duration", "pulse", "max_pulse", "calories"]
df = pd.read_csv("patient_data.csv", header=None, names=column_names)

#Inconsistent Data Types & Names
import pandas as pd 
df = pd.read_excel("C:/Users/sikha/css2024_day2/residentdoctors.xlsx")
print(df.info())

df["LOWER AGE"] = df["AGEDIST"].str.extract('(\d+)-')
df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)
print(df.info())

#Working wih dates

df = pd.read_csv("time_series_data.csv", index_col=0)
print(df.info())

df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")                           
  #The date/month/year ="%d-%m-%y

 #Another way to split the Date column into separate columns
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

#NANs (nothing was recorded) and Wrong Formats

import pandas as pd
#1.Remove extra index column
df = pd.read_csv("patient_data_dates.csv", index_col=0)
#3.Wrong data format
df.drop(index=26, inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
print(df.info())
#4. Wrong data 
df.loc[7, 'Duration'] = 45
alternatively:
df["Duration"]= df["Duration"].replace([450],50)
#5.Remove duplicates (11+12)
df.drop_duplicates(inplace = True)

#(2)Replace Empty Values(NANs) - Using fillna
avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace = True) 

#Removing Empty Cells – Using dropna
df.dropna(inplace = True)
df = df.reset_index(drop=True)

pd.set_option("display.max_rows", None) - used to show all of the data



"""
Aggregation
"""
df = pd.read_csv("iris.csv")
col_names = df.columns.tolist()


grouped = df.groupby("class")
#Calculate mean,sum & count squared values 
mean_squared_values = grouped['sepal_length'].mean()
sum_squared_values = grouped['sepal_length'].sum()
count_squared_values = grouped['sepal_length'].count()

#Display results 
print(mean_squared_values)
print(sum_squared_values)
print(count_squared_values)
"""
Append & Merge
"""

# Read the CSV files into dataframes
df1 = pd.read_csv("person_split1.csv")
df2 = pd.read_csv("person_split2.csv")

# Concatenate the dataframes
df = pd.concat([df1, df2], ignore_index=True)

#Merge 
df1 = pd.read_csv('person_education.csv')
df2 = pd.read_csv('person_work.csv')

## inner join
df_merge = pd.merge(df1,df2,on='id')

"""
Filtering
"""
df = pd.read_csv("iris.csv")

# Filter data for females
iris_versicolor = df[df['class'] == 'Iris-versicolor']

# Calculate the average iris_versicolor_sep_length
avg_iris_versicolor_sep_length = iris_versicolor['sepal_length'].mean()

#Alt label for class column 
df["class"] = df["class"].str.replace("Iris-", "")


df =df[df["sepal_length"] > 5]
df = df[df["class"] == "virginica"]

"""
Load
"""

df.to_csv("iris_data_cleaned.csv", index=False)

df.to_excel("iris_data_cleaned.xlsx", index=False, sheet_name='Sheet1')

df.to_json("iris_data_cleaned.json", orient='records')















