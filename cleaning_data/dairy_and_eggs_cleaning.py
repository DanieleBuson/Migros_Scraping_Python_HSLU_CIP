import pandas as pd
import numpy as np

eggDf = pd.read_csv("dairy_and_eggs.txt")

## extracting only products that have grams (or kilograms) for the following analysis

for i in range(len(eggDf)):
    # print(eggDf.loc[i, "Quantity"], "  ", type(eggDf.loc[i, "Quantity"]))
    if str(eggDf.loc[i, "Quantity"]).endswith("kg"):
        try:
            ## Frist of all, we need to extract all the data that can be found in the form of "number of values * single quantity"
            if len(eggDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(eggDf.loc[i, "Quantity"].split("x",1)[1].split("kg")[0].replace(" ", ""))*1000     
                number_of_values = float(eggDf.loc[i, "Quantity"].split("x")[0])
                eggDf.loc[i, "Quantity"] = single_value*number_of_values

            ## Having to deal with milk values, a keyword that can be used to check the result is "fat". 
            ## Once we split the string on this separator, we can check for the numerical input with the loop on
            ## the characters of the string, using also the indexing to cut in the proper way the result. 
            elif len(eggDf.loc[i, "Quantity"].split("fat")) > 1:
                temp_string = eggDf.loc[i, "Quantity"].split("fat",1)[1]
                eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("fat", 1)[0] + "fat"
                ind = 0
                count_number = 0
                for c in temp_string:
                    if c.isdigit() and count_number == 0:
                        eggDf.loc[i, "Product"] += temp_string[:ind]
                        eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("kg")[0])*1000
                        count_number+=1
                    ind += 1


            ## We extract then another word that is frequently appearing in the quantity, "slices". We are going to extract also "slices2 x"
            ## since a common issue is to have a combination of "slices" and "number of values * single quantity".
            elif len(eggDf.loc[i, "Quantity"].split("slices")) > 1:
                eggDf.loc[i,"Quantity"] = float(eggDf.loc[i, "Quantity"].split("slices",1)[1].split("kg")[0].replace(" ", ""))*1000

            elif len(eggDf.loc[i, "Quantity"].split("slices2 x")) > 1:
                eggDf.loc[i,"Quantity"] = 2*float(eggDf.loc[i, "Quantity"].split("slices2 x",1)[1].split("kg")[0].replace(" ", ""))*1000

            ## We want now to verify that there are 1 or two percentage. In both cases the procedure is the same we split the 
            ## string containing the quantity (the second or the third) into two parts checking with a for loop what is the first digit.
            ## Once it is find the first digit we cut the string using indexing.
            ## In this case, the use of a method to handle exception is fundamental, being not possible to manage all the cases, we do not
            ## want our program to crash.
            elif len(eggDf.loc[i, "Quantity"].split("%")) > 1:
                if len(eggDf.loc[i, "Quantity"].split("%")) == 2:
                    temp_string = eggDf.loc[i, "Quantity"].split("%", 1)[1]
                    eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("%", 1)[0] + "%"
                    ind = 0
                    count_number = 0
                    for c in temp_string:
                        if c.isdigit() and count_number == 0:
                            eggDf.loc[i, "Product"] += temp_string[:ind]
                            eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("kg")[0])*1000
                            count_number+=1
                        ind += 1
                elif len(eggDf.loc[i, "Quantity"].split("%")) == 3:
                    temp_string = eggDf.loc[i, "Quantity"].split("%", 2)[2]
                    eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("%", 2)[0] + "%" + eggDf.loc[i, "Quantity"].split("%", 2)[1] + "%"
                    ind = 0
                    count_number = 0
                    for c in temp_string:
                        if c.isdigit() and count_number == 0:
                            eggDf.loc[i, "Product"] += temp_string[:ind]
                            eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("kg")[0])*1000
                            count_number+=1
                        ind += 1

            else:
                eggDf.loc[i, "Quantity"] = float(eggDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000            
        except: 
            print("There is a problem with '", eggDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            eggDf.loc[i, "Quantity"] = np.nan

    elif str(eggDf.loc[i, "Quantity"])[-1] == "g" and str(eggDf.loc[i, "Quantity"])[-2] != "k":
        try: 
            if len(eggDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(eggDf.loc[i, "Quantity"].split("x",1)[1].split("g")[0].replace(" ", ""))
                number_of_values = float(eggDf.loc[i, "Quantity"].split("x")[0])
                eggDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(eggDf.loc[i, "Quantity"].split("fat")) > 1:
                temp_string = eggDf.loc[i, "Quantity"].split("fat",1)[1]
                eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("fat", 1)[0] + "fat"
                ind = 0
                count_number = 0
                for c in temp_string:
                    if c.isdigit() and count_number == 0:
                        eggDf.loc[i, "Product"] += temp_string[:ind]
                        eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("g")[0])
                        count_number+=1
                    ind += 1

            elif len(eggDf.loc[i, "Quantity"].split("slices")) > 1:
                eggDf.loc[i,"Quantity"] = float(eggDf.loc[i, "Quantity"].split("slices",1)[1].split("g")[0].replace(" ", ""))

            elif len(eggDf.loc[i, "Quantity"].split("slices2 x")) > 1:
                eggDf.loc[i,"Quantity"] = 2*float(eggDf.loc[i, "Quantity"].split("slices2 x",1)[1].split("g")[0].replace(" ", ""))

            elif len(eggDf.loc[i, "Quantity"].split("%")) > 1:
                if len(eggDf.loc[i, "Quantity"].split("%")) == 2:
                    temp_string = eggDf.loc[i, "Quantity"].split("%", 1)[1]
                    eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("%", 1)[0] + "%"
                    ind = 0
                    count_number = 0
                    for c in temp_string:
                        if c.isdigit() and count_number == 0:
                            eggDf.loc[i, "Product"] += temp_string[:ind]
                            eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("g")[0])
                            count_number+=1
                        ind += 1
                elif len(eggDf.loc[i, "Quantity"].split("%")) == 3:
                    temp_string = eggDf.loc[i, "Quantity"].split("%", 2)[2]
                    eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("%", 2)[0] + "%" + eggDf.loc[i, "Quantity"].split("%", 2)[1] + "%"
                    ind = 0
                    count_number = 0
                    for c in temp_string:
                        if c.isdigit() and count_number == 0:
                            eggDf.loc[i, "Product"] += temp_string[:ind]
                            eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("g")[0])
                            count_number+=1
                        ind += 1

            else:
                eggDf.loc[i, "Quantity"] = float(eggDf.loc[i, "Quantity"].split("g")[0].replace(" ", ""))
        except:
            print("There is a problem with '", eggDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            eggDf.loc[i, "Quantity"] = np.nan
    else: 
        eggDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
eggDf_grams = eggDf.dropna()
eggDf_grams = eggDf_grams.reset_index(drop = True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
# print(len(eggDf_grams))

with open("dairy_and_eggs_grams.txt", "w") as csv_file: 
    eggDf_grams.to_csv(csv_file)

## Extracting liters for following analysis

eggDf = pd.read_csv("dairy_and_eggs.txt")

for i in range(len(eggDf)):
    print(eggDf.loc[i, "Quantity"], "  ", type(eggDf.loc[i, "Quantity"]))
    ## In this case, we found out that the majority of records are in ml and l. However, there are some records in dl. We are going,
    ## therefore, to extract records that terminate with this three suffixes.
    if str(eggDf.loc[i, "Quantity"]).endswith("ml"):
        try:
            ## As usaul, we use the x when we have to extract values that are in the form "number of values* quantity of the single value".
            ## In a second moment we perform the product and store the result as a float in the pandas dataframe. 
            if len(eggDf.loc[i, "Quantity"].split("x"))>1:
                single_value = float(eggDf.loc[i, "Quantity"].split("x")[1].split("ml")[0].replace(" ", ""))/1000
                number_of_values = float(eggDf.loc[i, "Quantity"].split("x")[0])
                eggDf.loc[i, "Quantity"] = single_value*number_of_values

            ## We can also use the percentage of milk (percentage of fat) to extract the quantity value. It was
            ## possible to do the same with "fat", however, we needed to handle diffefrent possibilities of lower and upper cases.
            elif len(eggDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = eggDf.loc[i, "Quantity"].split("%", 1)[1]
                eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("%")[0] + "%"
                ind = 0
                count_number = 0
                for c in temp_string:
                    if c.isdigit() and count_number == 0:
                        eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("ml")[0])/1000
                        eggDf.loc[i, "Product"] += temp_string[:ind]
                        count_number += 1
                    ind += 1

            else:
                eggDf.loc[i, "Quantity"] = float(eggDf.loc[i, "Quantity"].split("ml")[0].replace(" ", ""))/1000
        except: 
            print("There is a problem with '", eggDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            eggDf.loc[i, "Quantity"] = np.nan

    elif str(eggDf.loc[i, "Quantity"]).endswith("dl"):
        try:
            if len(eggDf.loc[i, "Quantity"].split("x"))>1:
                single_value = float(eggDf.loc[i, "Quantity"].split("x")[1].split("dl")[0].replace(" ", ""))/10
                number_of_values = float(eggDf.loc[i, "Quantity"].split("x")[0])
                eggDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(eggDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = eggDf.loc[i, "Quantity"].split("%", 1)[1]
                eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("%")[0] + "%"
                ind = 0
                count_number = 0
                for c in temp_string:
                    if c.isdigit() and count_number == 0:
                        eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("dl")[0])/10
                        eggDf.loc[i, "Product"] += temp_string[:ind]
                        count_number += 1
                    ind += 1


            else:
                eggDf.loc[i, "Quantity"] = float(eggDf.loc[i, "Quantity"].split("dl")[0].replace(" ", ""))/10
        except: 
            print("There is a problem with '", eggDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            eggDf.loc[i, "Quantity"] = np.nan


    elif str(eggDf.loc[i, "Quantity"])[-1] == "l" and str(eggDf.loc[i, "Quantity"])[-2] != "m":
        try: 
            if len(eggDf.loc[i, "Quantity"].split("x"))>1:
                single_value = float(eggDf.loc[i, "Quantity"].split("x")[1].split("l")[0].replace(" ", ""))
                number_of_values = float(eggDf.loc[i, "Quantity"].split("x")[0])
                eggDf.loc[i, "Quantity"] = single_value*number_of_values

            elif len(eggDf.loc[i, "Quantity"].split("%"))>1:
                temp_string = eggDf.loc[i, "Quantity"].split("%", 1)[1]
                eggDf.loc[i, "Product"] += eggDf.loc[i, "Quantity"].split("%")[0] + "%"
                ind = 0
                count_number = 0
                for c in temp_string:
                    if c.isdigit() and count_number == 0:
                        eggDf.loc[i, "Quantity"] = float(temp_string[ind:].split("l")[0])
                        eggDf.loc[i, "Product"] += temp_string[:ind]
                        count_number += 1
                    ind += 1

            else:
                eggDf.loc[i, "Quantity"] = float(eggDf.loc[i, "Quantity"].split("l")[0].replace(" ", ""))
        except:
            print("There is a problem with '", eggDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            eggDf.loc[i, "Quantity"] = np.nan
    else: 
        eggDf.loc[i, "Quantity"] = np.nan


## We drop all the rows with a na value and then we reset the indexing. 
eggDf_liter = eggDf.dropna()
eggDf_liter = eggDf_liter.reset_index(drop=True)

# print(len(eggDf_liter))

with open("dairy_and_eggs_liters.txt", "w") as csv_file:
    eggDf_liter.to_csv(csv_file)

