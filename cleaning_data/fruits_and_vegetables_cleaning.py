import pandas as pd
import numpy as np

vegDf = pd.read_csv("fruits_and_vegetables.txt")

## extracting only products that have grams (or kilograms) for the following analysis

for i in range(len(vegDf)):
    print(vegDf.loc[i, "Quantity"], "  ", type(vegDf.loc[i, "Quantity"]))
    if str(vegDf.loc[i, "Quantity"]).endswith("kg"):
        try:
            ## We check only the case we have the "number of values* single value quantity". 
            ## In case we store the product. Alternatively, it is possible to store the value 
            ## in float form. As usual, we define the try except statement in order not to 
            ## crash the program
            if len(vegDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(vegDf.loc[i, "Quantity"].split("x")[1].split("kg")[0].replace(" ", ""))*1000
                number_of_values = float(vegDf.loc[i, "Quantity"].split("x")[0])
                vegDf.loc[i, "Quantity"] =  float(single_value*number_of_values)
            else:
                vegDf.loc[i, "Quantity"] = float(vegDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000            
        except: 
            print("There is a problem with '", vegDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            vegDf.loc[i, "Quantity"] = np.nan
    elif str(vegDf.loc[i, "Quantity"])[-1] == "g" and str(vegDf.loc[i, "Quantity"])[-2] != "k":
        try: 
            if len(vegDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(vegDf.loc[i, "Quantity"].split("x")[1].split("g")[0].replace(" ", ""))
                number_of_values = float(vegDf.loc[i, "Quantity"].split("x")[0])
                vegDf.loc[i, "Quantity"] =  float(single_value*number_of_values)
            else:
                vegDf.loc[i, "Quantity"] = float(vegDf.loc[i, "Quantity"].split("g")[0].replace(" ", "")) 
        except:
            print("There is a problem with '", vegDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            vegDf.loc[i, "Quantity"] = np.nan
    else: 
        vegDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
vegDf_grams = vegDf.dropna()
vegDf_grams = vegDf_grams.reset_index(drop = True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
# print(len(vegDf_grams))

with open("fruits_and_vegetables_grams.txt", "w") as csv_file:
    vegDf_grams.to_csv(csv_file)

## Extracting liters for following analysis

vegDf = pd.read_csv("fruits_and_vegetables.txt")

for i in range(len(vegDf)):
    # print(vegDf.loc[i, "Quantity"], "  ", type(vegDf.loc[i, "Quantity"]))
    if str(vegDf.loc[i, "Quantity"]).endswith("ml"):
        ## In this case the extraction of data is perfect (no error). However we have just a few results as expected
        ## (not common to measure something that is in the vegetables area of a supermarket in liters)
        try:
            vegDf.loc[i, "Quantity"] = float(vegDf.loc[i, "Quantity"].split("ml")[0].replace(" ", ""))/1000
        except: 
            print("There is a problem with '", vegDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            vegDf.loc[i, "Quantity"] = np.nan
    elif str(vegDf.loc[i, "Quantity"])[-1] == "l" and str(vegDf.loc[i, "Quantity"])[-2] != "m":
        try: 
            vegDf.loc[i, "Quantity"] = float(vegDf.loc[i, "Quantity"].split("l")[0].replace(" ", ""))
        except:
            print("There is a problem with '", vegDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            vegDf.loc[i, "Quantity"] = np.nan
    else: 
        vegDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
vegDf_liter = vegDf.dropna()
vegDf_liter = vegDf_liter.reset_index(drop=True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
# print(len(vegDf_liter))

with open("fruits_and_vegetables_liters.txt", "w") as csv_file:
    vegDf_liter.to_csv(csv_file)