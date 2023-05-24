import pandas as pd
import numpy as np

snacksDf = pd.read_csv("data/snacks_and_sweets.txt")

# extracting only products that have grams (or kilograms) for the following analysis

for i in range(len(snacksDf)):
    # print(snacksDf.loc[i, "Quantity"], "  ", type(snacksDf.loc[i, "Quantity"]))
    if str(snacksDf.loc[i, "Quantity"]).endswith("kg"):
        try:
            ## First of all we search for the form "number of values * single value quantity" and then we 
            ## perform the product to extract the exact quantity
            if len(snacksDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(snacksDf.loc[i, "Quantity"].split("x")[1].split("kg")[0].replace(" ", ""))*1000
                number_of_values = float(snacksDf.loc[i, "Quantity"].split("x")[0])
                snacksDf.loc[i, "Quantity"] = single_value*number_of_values

            ## Another issue that can arise is the presence of a percentage in the string. Therefore, we cut on the percentage 
            ## so that it is possible to extract the value.
            elif len(snacksDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = snacksDf.loc[i, "Quantity"].split("%")[1]
                snacksDf.loc[i, "Product"] += snacksDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        snacksDf.loc[i, "Quantity"] = float(temp_string[ind:].split("kg")[0])*1000
                        snacksDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1

            else: 
                snacksDf.loc[i, "Quantity"] = float(snacksDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000
        except: 
            print("There is a problem with '", snacksDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            snacksDf.loc[i, "Quantity"] = np.nan
    elif str(snacksDf.loc[i, "Quantity"])[-1] == "g" and str(snacksDf.loc[i, "Quantity"])[-2] != "k":
        try: 
            if len(snacksDf.loc[i, "Quantity"].split("x"))>1:
                single_value =  float(snacksDf.loc[i, "Quantity"].split("x")[1].split("g")[0].replace(" ", ""))
                number_of_values = float(snacksDf.loc[i, "Quantity"].split("x")[0])
                snacksDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(snacksDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = snacksDf.loc[i, "Quantity"].split("%")[1]
                snacksDf.loc[i, "Product"] += snacksDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        snacksDf.loc[i, "Quantity"] = float(temp_string[ind:].split("g")[0])
                        snacksDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1

            else: 
                snacksDf.loc[i, "Quantity"] = float(snacksDf.loc[i, "Quantity"].split("g")[0].replace(" ", ""))
        except:
            print("There is a problem with '", snacksDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            snacksDf.loc[i, "Quantity"] = np.nan
    else: 
        snacksDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
snacksDf_grams = snacksDf.dropna()
snacksDf_grams = snacksDf_grams.reset_index(drop = True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
print(len(snacksDf_grams))

with open("data/snacks_and_sweets_grams.txt", "w") as csv_file:
    snacksDf_grams.to_csv(csv_file)

## No liters in this case.
