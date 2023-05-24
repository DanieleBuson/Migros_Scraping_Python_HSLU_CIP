import pandas as pd
import numpy as np

frozenDf = pd.read_csv("data/frozen_food.txt")

## extracting only products that have grams (or kilograms) for the following analysis

for i in range(len(frozenDf)):
    print(frozenDf.loc[i, "Quantity"], "  ", type(frozenDf.loc[i, "Quantity"]))
    if str(frozenDf.loc[i, "Quantity"]).endswith("kg"):
        try:
            ## The first case that we are going to extract is the "number of values * single value quantity". We do it through  
            ## splitting the strings on the x separator. 
            if len(frozenDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(frozenDf.loc[i, "Quantity"].split("x")[1].split("kg")[0].replace(" ", ""))*1000
                number_of_values = float(frozenDf.loc[i, "Quantity"].split("x")[0])
                frozenDf.loc[i, "Quantity"] = single_value*number_of_values

            ## The other case we are going to consider is the possibility to cut the strings on the separator 
            ## "pieces".
            elif len(frozenDf.loc[i, "Quantity"].split("pieces"))>1:
                frozenDf.loc[i, "Quantity"] = float(frozenDf.loc[i, "Quantity"].split("pieces")[1].split("kg")[0].replace(" ", ""))*1000

            else: 
                frozenDf.loc[i, "Quantity"] = float(frozenDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000
        except: 
            print("There is a problem with '", frozenDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            frozenDf.loc[i, "Quantity"] = np.nan
    elif str(frozenDf.loc[i, "Quantity"])[-1] == "g" and str(frozenDf.loc[i, "Quantity"])[-2] != "k":
        try: 
            if len(frozenDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(frozenDf.loc[i, "Quantity"].split("x")[1].split("g")[0].replace(" ", ""))
                number_of_values = float(frozenDf.loc[i, "Quantity"].split("x")[0])
                frozenDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(frozenDf.loc[i, "Quantity"].split("pieces"))>1:
                frozenDf.loc[i, "Quantity"] = float(frozenDf.loc[i, "Quantity"].split("pieces")[1].split("g")[0].replace(" ", ""))

            else: 
                frozenDf.loc[i, "Quantity"] = float(frozenDf.loc[i, "Quantity"].split("g")[0].replace(" ", ""))
        except:
            print("There is a problem with '", frozenDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            frozenDf.loc[i, "Quantity"] = np.nan
    else: 
        frozenDf.loc[i, "Quantity"] = np.nan


## The following steps are dropping all the rows containing a na and reset pandas indexing
frozenDf_grams = frozenDf.dropna()
frozenDf_grams = frozenDf_grams.reset_index(drop = True)

## Decommenting this line you can check the number of records. 
print(len(frozenDf_grams))

with open("data/frozen_food_grams.txt", "w") as csv_file:
    frozenDf_grams.to_csv(csv_file)

## Extracting liters for following analysis

frozenDf = pd.read_csv("data/frozen_food.txt")

for i in range(len(frozenDf)):
    print(frozenDf.loc[i, "Quantity"], "  ", type(frozenDf.loc[i, "Quantity"]))
    ## Also in this case we are going to extract a dataframe for liters. We are going to check ml and l.
    ## In this case we do not need more than what is written below. The main reason is that the loss of information is minimal. 
    ## Therefore, we concentrated our time resources on other cleaning processes. 
    if str(frozenDf.loc[i, "Quantity"]).endswith("ml"):
        try:
            if len(frozenDf.loc[i, "Quantity"].split(" x "))>1:
                single_value =  float(frozenDf.loc[i, "Quantity"].split(" x ")[1].split("ml")[0].replace(" ", ""))/1000
                number_of_values = float(frozenDf.loc[i, "Quantity"].split(" x ")[0])
                frozenDf.loc[i, "Quantity"] = single_value*number_of_values
            else: 
                frozenDf.loc[i, "Quantity"] = float(frozenDf.loc[i, "Quantity"].split("ml")[0].replace(" ", ""))/1000
        except: 
            print("There is a problem with '", frozenDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            frozenDf.loc[i, "Quantity"] = np.nan
    elif str(frozenDf.loc[i, "Quantity"])[-1] == "l" and str(frozenDf.loc[i, "Quantity"])[-2] != "m":
        try: 
            if len(frozenDf.loc[i, "Quantity"].split(" x "))>1:
                single_value =  float(frozenDf.loc[i, "Quantity"].split(" x ")[1].split("l")[0].replace(" ", ""))
                number_of_values = float(frozenDf.loc[i, "Quantity"].split(" x ")[0])
                frozenDf.loc[i, "Quantity"] = single_value*number_of_values
            else: 
                frozenDf.loc[i, "Quantity"] = float(frozenDf.loc[i, "Quantity"].split("l")[0].replace(" ", ""))
        except:
            print("There is a problem with '", frozenDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            frozenDf.loc[i, "Quantity"] = np.nan
    else: 
        frozenDf.loc[i, "Quantity"] = np.nan

## The following steps are dropping all the rows containing a na and reset pandas indexing
frozenDf_liter = frozenDf.dropna()
frozenDf_liter = frozenDf_liter.reset_index(drop=True)

## Decommenting this line you can check the number of records. 
print(len(frozenDf_liter))

with open("data/frozen_food_liters.txt", "w") as csv_file:
    frozenDf_liter.to_csv(csv_file)

