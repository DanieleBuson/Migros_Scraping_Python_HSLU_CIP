import pandas as pd
import numpy as np

breadDf = pd.read_csv("data/bread_and_pastries.txt")

## extracting only products that have grams (or kilograms) for the following analysis
## It is important to extract the quantities in order to gain information regarding the price per g or kg.

for i in range(len(breadDf)):
    # print(breadDf.loc[i, "Quantity"], "  ", type(breadDf.loc[i, "Quantity"]))

    ## First of all we check the end of the strings. We handle these strings only if they end with "g" or "kg"
    if str(breadDf.loc[i, "Quantity"]).endswith("kg"):
        ## To avoid any errors related to type, we wrapped our code into the try-except statement. 
        ## In case something goes wrong the code is able to alert the user and add a np.nan value in the column.
        try:
            ## We observed that lot of records were containing an x ( ex 2x100g). We decided to handle
            ## this particular case extracting the data regarding the number of values and the quantity of the single value. 
            ## In the end, we multiply the two numbers into the final result. 
            ## In order to understand when is the case we use the function split. If the function creates a list of one single element
            ## it means that the character/s of the separator is not inside the string. Therefore, if the list created has more than 2
            ## elements it is the case to cut.


            if len(breadDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(breadDf.loc[i, "Quantity"].split("x", 1)[1].split("kg")[0].replace(" ", ""))*1000
                number_of_values = float(breadDf.loc[i, "Quantity"].split("x")[0])
                breadDf.loc[i, "Quantity"] =  single_value*number_of_values


            ## Another possibility was the er. We observed that many product have the er before the quantity. 
            ## It is important to store the product before the quantity or we are going to end up in the except section of the code for 
            ## a type error.
            elif len(breadDf.loc[i, "Quantity"].split("er")) > 1:
                breadDf.loc[i, "Product"] += breadDf.loc[i, "Quantity"].split("er")[0] + "er"
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("er")[1].split("kg")[0].replace(" ", ""))*1000

            elif len(breadDf.loc[i, "Quantity"].split("Stück")) > 1:
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("Stück")[1].split("kg")[0].replace(" ", ""))*1000

            ## Another possibility is having the percentage
            elif len(breadDf.loc[i, "Quantity"].split("%")) > 1:
                temp_string = breadDf.loc[i, "Quantity"].split("%")[1]
                breadDf.loc[i, "Product"] += breadDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        breadDf.loc[i, "Quantity"] = float(temp_string[ind:].split("kg")[0])*1000
                        breadDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1
                
            ## We decided for time reasons, not to extract other records that were problematic. However, we believe that in a larger project
            ## all the cases have to be considered.
            else:
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000
        except: 
            # print("There is a problem with '", breadDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            breadDf.loc[i, "Quantity"] = np.nan
    
    ## We did the same consideration for grams. 
    elif str(breadDf.loc[i, "Quantity"])[-1] == "g" and str(breadDf.loc[i, "Quantity"])[-2] != "k":
        try:
            if len(breadDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(breadDf.loc[i, "Quantity"].split("x", 1)[1].split("g")[0].replace(" ", ""))
                number_of_values = float(breadDf.loc[i, "Quantity"].split("x")[0])
                breadDf.loc[i, "Quantity"] =  single_value*number_of_values

            elif len(breadDf.loc[i, "Quantity"].split("er")) > 1:
                breadDf.loc[i, "Product"] += breadDf.loc[i, "Quantity"].split("er")[0] + "er"
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("er")[1].split("g")[0].replace(" ", ""))
                
            elif len(breadDf.loc[i, "Quantity"].split("Stück")) > 1:
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("Stück")[1].split("g")[0].replace(" ", ""))

            elif len(breadDf.loc[i, "Quantity"].split("%")) > 1:
                temp_string = breadDf.loc[i, "Quantity"].split("%")[1]
                breadDf.loc[i, "Product"] += breadDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        breadDf.loc[i, "Quantity"] = float(temp_string[ind:].split("g")[0])
                        breadDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1

            else:
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("g")[0].replace(" ", ""))
        except:
            # print("There is a problem with '", breadDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            breadDf.loc[i, "Quantity"] = np.nan
    
    ## since we are searching for grams or kilograms, if the termination of the quantity is different (in pieces or liters)
    ## we just store the value na
    else: 
        breadDf.loc[i, "Quantity"] = np.nan


## The following steps are dropping all the rows containing a na and reset pandas indexing
breadDf_grams = breadDf.dropna()
breadDf_grams = breadDf_grams.reset_index(drop = True)

## We can check here, decommenting the code, how many values we have in the new dataframe.
# print(len(breadDf_grams))

## After creating the dataframe, we can store it temporarily in a csv file. 

with open("data/bread_and_pastries_grams.txt", "w") as csv_file:
    breadDf_grams.to_csv(path_or_buf=csv_file)
    print("Done! CSV created")


# Extracting liters for following analysis
# The purpose is the same as before, extracting all the values in liters to have the possibility to show 
# numerical data regarding the price per liter.

breadDf = pd.read_csv("data/bread_and_pastries.txt")

for i in range(len(breadDf)):
    # print(breadDf.loc[i, "Quantity"], "  ", type(breadDf.loc[i, "Quantity"]))
    ## In this case we do not have many records in ml/l. Therefore we only check for the x "operator" to perform the 
    ## product between the two possible numbers.
    if str(breadDf.loc[i, "Quantity"]).endswith("ml"):
        try:
            if len(breadDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(breadDf.loc[i, "Quantity"].split("x")[1].split("ml")[0].replace(" ", ""))/1000
                number_of_values = float(breadDf.loc[i, "Quantity"].split("x")[0])
                breadDf.loc[i, "Quantity"] =  float(single_value*number_of_values)
                
            else:
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("ml")[0].replace(" ", ""))/1000

        except: 
            # print("There is a problem with '", breadDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            breadDf.loc[i, "Quantity"] = np.nan

    elif str(breadDf.loc[i, "Quantity"])[-1] == "l" and str(breadDf.loc[i, "Quantity"])[-2] != "m":
        try: 
            if len(breadDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(breadDf.loc[i, "Quantity"].split("x")[1].split("l")[0].replace(" ", ""))
                number_of_values = float(breadDf.loc[i, "Quantity"].split("x")[0])
                breadDf.loc[i, "Quantity"] =  float(single_value*number_of_values)

            else:
                breadDf.loc[i, "Quantity"] = float(breadDf.loc[i, "Quantity"].split("l")[0].replace(" ", ""))

        except:
            # print("There is a problem with '", breadDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            breadDf.loc[i, "Quantity"] = np.nan

    else: 
        breadDf.loc[i, "Quantity"] = np.nan


breadDf_liter = breadDf.dropna()
breadDf_liter = breadDf_liter.reset_index(drop=True)

## Decommenting this line you can check the number of records. 
# print(len(breadDf_liter))

## After creating the dataframe, we can store it temporarily in a csv file. 

with open("data/bread_and_pastries_liters.txt", "w") as csv_file:
    breadDf_liter.to_csv(path_or_buf=csv_file)
    print("Done! CSV created")
