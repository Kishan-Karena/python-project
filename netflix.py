import pandas as pd

data=pd.read_csv("netflix1.csv")

data.head()

data.tail()

data.info()

"""Deleting redundant columns.
Renaming the columns.
Dropping duplicates.
Remove the Nan values from the dataset."""

data.head(1)

data.columns
data.drop(columns="rating",inplace=True)
data.head()

data.columns

new_column_names=[]

for i in data.columns:
    new_column_names.append(i.capitalize())

new_column_names

data.columns=new_column_names

data.head()

data.duplicated().sum()

# For cleaning duplicate
data.drop_duplicates(inplace=True)
data.isna().sum()

data["Show_id"].unique()
data.dropna(inplace=True)
data["Date_added"]= data["Date_added"].apply(lambda x: x.replace("/","-"))
data

df=data["Country"].value_counts().reset_index()
df[df["Country"]=="India"]

data.to_csv("Cleaned_Data_Csv.csv",index=False)