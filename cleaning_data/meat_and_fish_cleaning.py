import pandas as pd
import numpy as np

meatDf = pd.read_csv("data/fish_and_meat.txt")

## extracting only products that have grams (or kilograms) for the following analysis

for i in range(len(meatDf)):
    # print(meatDf.loc[i, "Quantity"], "  ", type(meatDf.loc[i, "Quantity"]))
    if str(meatDf.loc[i, "Quantity"]).endswith("kg"):
        try:
            ## In this case we check for some words such as "Stück", "pieces", "pièces".
            if len(meatDf.loc[i, "Quantity"].split("Stück")) > 1:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("Stück",2)[1].split("kg")[0].replace(" ", ""))*1000

            elif len(meatDf.loc[i, "Quantity"].split("pieces")) > 1:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("pieces")[1].split("kg")[0].replace(" ", ""))*1000

            elif len(meatDf.loc[i, "Quantity"].split("pièces")) > 1:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("pièces")[1].split("kg")[0].replace(" ", ""))*1000

            ## The next step would be to extract all the product in the form "number of values* sinle value quantity".
            ## Once these records are located in the pandas dataframe we can perform the product to extract the grams.
            elif len(meatDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(meatDf.loc[i, "Quantity"].split("x")[1].split("kg")[0].replace(" ", ""))*1000
                number_of_values = float(meatDf.loc[i, "Quantity"].split("x")[0])
                meatDf.loc[i, "Quantity"] =  float(single_value*number_of_values)

            else:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000
        except: 
            print("There is a problem with '", meatDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            meatDf.loc[i, "Quantity"] = np.nan
    elif str(meatDf.loc[i, "Quantity"])[-1] == "g" and str(meatDf.loc[i, "Quantity"])[-2] != "k":
        try: 
            if len(meatDf.loc[i, "Quantity"].split("Stück"))>1:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("Stück",2)[1].split("g")[0].replace(" ", ""))

            elif len(meatDf.loc[i, "Quantity"].split("pieces")) > 1:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("pieces")[1].split("g")[0].replace(" ", ""))

            elif len(meatDf.loc[i, "Quantity"].split("pièces")) > 1:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("pièces")[1].split("g")[0].replace(" ", ""))

            elif len(meatDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(meatDf.loc[i, "Quantity"].split("x")[1].split("g")[0].replace(" ", ""))
                number_of_values = float(meatDf.loc[i, "Quantity"].split("x")[0])
                meatDf.loc[i, "Quantity"] =  float(single_value*number_of_values)

            else:
                meatDf.loc[i, "Quantity"] = float(meatDf.loc[i, "Quantity"].split("g")[0].replace(" ", ""))
        except:
            print("There is a problem with '", meatDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            meatDf.loc[i, "Quantity"] = np.nan
    else: 
        meatDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
meatDf_grams = meatDf.dropna()
meatDf_grams = meatDf_grams.reset_index(drop=True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
# print(len(meatDf_grams))

with open("data/fish_and_meat_grams.txt", "w") as csv_file:
    meatDf_grams.to_csv(csv_file)

## No liter in the meat