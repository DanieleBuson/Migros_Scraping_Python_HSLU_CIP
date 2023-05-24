import pandas as pd
import numpy as np

pastaDf = pd.read_csv("data/pasta_and_canned.txt")

## extracting only products that have grams (or kilograms) for the following analysis

for i in range(len(pastaDf)):
    # print(pastaDf.loc[i, "Quantity"], "  ", type(pastaDf.loc[i, "Quantity"]))
    if str(pastaDf.loc[i, "Quantity"]).endswith("kg"):
        try:
            ## As it was for other scripts, we start from extracting the x-es in order to perform the product
            ## between the number of value and the single value quantity.
            if len(pastaDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(pastaDf.loc[i, "Quantity"].split("x")[1].split("kg")[0].replace(" ", ""))*1000
                number_of_values = float(pastaDf.loc[i, "Quantity"].split("x")[0])
                pastaDf.loc[i, "Quantity"] = single_value*number_of_values

            ##Then it is useful to cut to the words "pieces", "G" and "liters" since lot of records have these issues. 
            elif len(pastaDf.loc[i, "Quantity"].split("pieces"))>1:
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("pieces")[1].split("kg")[0].replace(" ", ""))*1000

            elif len(pastaDf.loc[i, "Quantity"].split("liters"))>1:
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("liters")[1].split("kg")[0].replace(" ", ""))*1000

            elif len(pastaDf.loc[i, "Quantity"].split("G"))>1:
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("G")[1].split("kg")[0].replace(" ", ""))*1000

            else: 
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000
        except: 
            print("There is a problem with '", pastaDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            pastaDf.loc[i, "Quantity"] = np.nan

    elif str(pastaDf.loc[i, "Quantity"])[-1] == "g" and str(pastaDf.loc[i, "Quantity"])[-2] != "k":
        try: 
            if len(pastaDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(pastaDf.loc[i, "Quantity"].split("x")[1].split("g")[0].replace(" ", ""))
                number_of_values = float(pastaDf.loc[i, "Quantity"].split("x")[0])
                pastaDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(pastaDf.loc[i, "Quantity"].split("pieces"))>1:
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("pieces")[1].split("g")[0].replace(" ", ""))

            elif len(pastaDf.loc[i, "Quantity"].split("liters"))>1:
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("liters")[1].split("g")[0].replace(" ", ""))

            elif len(pastaDf.loc[i, "Quantity"].split("G"))>1:
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("G")[1].split("g")[0].replace(" ", ""))

            else: 
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("g")[0].replace(" ", ""))
        except:
            print("There is a problem with '", pastaDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            pastaDf.loc[i, "Quantity"] = np.nan
    else: 
        pastaDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
pastaDf_grams = pastaDf.dropna()
pastaDf_grams = pastaDf_grams.reset_index(drop = True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
print(len(pastaDf_grams))

with open("data/pasta_and_canned_grams.txt", "w") as csv_file:
    pastaDf_grams.to_csv(csv_file)

## Extracting liters for following analysis

pastaDf = pd.read_csv("data/pasta_and_canned.txt")

for i in range(len(pastaDf)):
    # print(pastaDf.loc[i, "Quantity"], "  ", type(pastaDf.loc[i, "Quantity"]))
    ## We are going to extract the value from all the strings that terminate with ml, cl and l. 
    ## All the other cases are identical to the one of "ml". Therefore, only this will be commented.
    if str(pastaDf.loc[i, "Quantity"]).endswith("ml"):
        try:
            ## The first case we are going to consider is "nnumber of values * single value quantity". 
            if len(pastaDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(pastaDf.loc[i, "Quantity"].split("x")[1].split("ml")[0].replace(" ", ""))/1000
                number_of_values = float(pastaDf.loc[i, "Quantity"].split("x")[0])
                pastaDf.loc[i, "Quantity"] = single_value*number_of_values

            ## We also check for the presence of a percentage.
            elif len(pastaDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = pastaDf.loc[i, "Quantity"].split("%")[1]
                pastaDf.loc[i, "Product"] += pastaDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        pastaDf.loc[i, "Quantity"] = float(temp_string[ind:].split("ml")[0])/1000
                        pastaDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1

            else: 
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("ml")[0].replace(" ", ""))/1000
        except: 
            print("There is a problem with '", pastaDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            pastaDf.loc[i, "Quantity"] = np.nan

    elif str(pastaDf.loc[i, "Quantity"]).endswith("cl"):
        try:
            if len(pastaDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(pastaDf.loc[i, "Quantity"].split("x")[1].split("cl")[0].replace(" ", ""))/100
                number_of_values = float(pastaDf.loc[i, "Quantity"].split("x")[0])
                pastaDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(pastaDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = pastaDf.loc[i, "Quantity"].split("%")[1]
                pastaDf.loc[i, "Product"] += pastaDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        pastaDf.loc[i, "Quantity"] = float(temp_string[ind:].split("cl")[0])/100
                        pastaDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1

            else: 
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("cl")[0].replace(" ", ""))/100
        except: 
            print("There is a problem with '", pastaDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            pastaDf.loc[i, "Quantity"] = np.nan

    elif str(pastaDf.loc[i, "Quantity"])[-1] == "l" and (str(pastaDf.loc[i, "Quantity"])[-2] != "m" or str(pastaDf.loc[i, "Quantity"])[-2] != "c"):
        try: 
            if len(pastaDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(pastaDf.loc[i, "Quantity"].split("x")[1].split("l")[0].replace(" ", ""))
                number_of_values = float(pastaDf.loc[i, "Quantity"].split("x")[0])
                pastaDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(pastaDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = pastaDf.loc[i, "Quantity"].split("%")[1]
                pastaDf.loc[i, "Product"] += pastaDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        pastaDf.loc[i, "Quantity"] = float(temp_string[ind:].split("l")[0])
                        pastaDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1

            else: 
                pastaDf.loc[i, "Quantity"] = float(pastaDf.loc[i, "Quantity"].split("l")[0].replace(" ", ""))
        except:
            print("There is a problem with '", pastaDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            pastaDf.loc[i, "Quantity"] = np.nan
    else: 
        pastaDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
pastaDf_liter = pastaDf.dropna()
pastaDf_liter = pastaDf_liter.reset_index(drop=True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
print(len(pastaDf_liter))

with open("data/pasta_and_canned_liters.txt", "w") as csv_file:
    pastaDf_liter.to_csv(csv_file)

