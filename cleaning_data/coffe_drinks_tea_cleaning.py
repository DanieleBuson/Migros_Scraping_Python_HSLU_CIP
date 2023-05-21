import pandas as pd
import numpy as np

coffeDf = pd.read_csv("coffe_drinks_tea.txt")

## extracting only products that have grams (or kilograms) for the following analysis

for i in range(len(coffeDf)):
    print(coffeDf.loc[i, "Quantity"], "  ", type(coffeDf.loc[i, "Quantity"]))
    ## We check if the string in quantity is ends with "kg". In case, we will check different cases
    if str(coffeDf.loc[i, "Quantity"]).endswith("kg"):
        try:
            ## A common case is the "x". We extract the quantity and the numebr of pieces. Then, we perform the product between
            ## the two numbers. 
            if len(coffeDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(coffeDf.loc[i, "Quantity"].split("x")[1].split("kg")[0].replace(" ", ""))*1000
                number_of_values = float(coffeDf.loc[i, "Quantity"].split("x")[0])
                coffeDf.loc[i, "Quantity"] =  float(single_value*number_of_values)

            ## Other interesting cases are "intensity" and "strangth". Extracting the word we can have more information on the product
            ## and at the same time, having the right quantity.
            ## Also in this case the fact that we store the product value in advance is crucial to make the code work.
            elif len(coffeDf.loc[i, "Quantity"].split("intensity")) > 1:
                coffeDf.loc[i, "Product"] += coffeDf.loc[i, "Quantity"].split("intensity")[0] + " intensity"
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("intensity")[1].split("kg")[0].replace(" ", ""))*1000

            elif len(coffeDf.loc[i, "Quantity"].split("strength")) > 1:
                coffeDf.loc[i, "Product"] += coffeDf.loc[i, "Quantity"].split("strength")[0] + " strength"
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("strength")[1].split("kg")[0].replace(" ", ""))*1000

            ## The % are usually one of the reasons why we have problems in data extraction, cutting on numbers. 
            ## Therefore, we decided to extract all the records with just one percentage and store them correctly in product
            ## and quantity fields.
            elif len(coffeDf.loc[i, "Quantity"].split("%")) > 1:
                temp_string = coffeDf.loc[i, "Quantity"].split("%")[1]
                coffeDf.loc[i, "Product"] += coffeDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    ## We search for a digit and cut the string.
                    if c.isdigit() and count_number == 0:
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("kg")[0])*1000
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        ## Setting the count number to 1 we avoid the search of another digit.
                        count_number += 1
                    ind += 1
            
            ## Other cases: BTL and KG.
            elif len(coffeDf.loc[i, "Quantity"].split("BTL")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("BTL")[1].split("kg")[0].replace(" ", ""))*1000

            elif len(coffeDf.loc[i, "Quantity"].split("KG")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("KG")[1].split("kg")[0].replace(" ", ""))*1000

            ## last, but not least, the "Pads" cases. 
            elif len(coffeDf.loc[i, "Quantity"].split("Pads")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("Pads")[1].split("kg")[0].replace(" ", ""))*1000

            ## In case we are not in any of the previous cases we just store the result. 
            else:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("kg")[0].replace(" ", ""))*1000
        
        ## We will handle any error that can arise catching an exception and inserting the value np.nan instead of letting
        ## the program to crash.
        except: 
            print("There is a problem with '", coffeDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            coffeDf.loc[i, "Quantity"] = np.nan

    ## Same process for the grams
    elif str(coffeDf.loc[i, "Quantity"])[-1] == "g" and str(coffeDf.loc[i, "Quantity"])[-2] != "k":
        try: 
            if len(coffeDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(coffeDf.loc[i, "Quantity"].split("x")[1].split("g")[0].replace(" ", ""))
                number_of_values = float(coffeDf.loc[i, "Quantity"].split("x")[0])
                coffeDf.loc[i, "Quantity"] =  float(single_value*number_of_values)

            elif len(coffeDf.loc[i, "Quantity"].split("intensity")) > 1:
                coffeDf.loc[i, "Product"] += coffeDf.loc[i, "Quantity"].split("intensity")[0] + " intensity"
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("intensity")[1].split("g")[0].replace(" ", ""))

            elif len(coffeDf.loc[i, "Quantity"].split("strength")) > 1:
                coffeDf.loc[i, "Product"] += coffeDf.loc[i, "Quantity"].split("strength")[0] + " strength"
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("strength")[1].split("g")[0].replace(" ", ""))

            elif len(coffeDf.loc[i, "Quantity"].split("%")) > 1:
                temp_string = coffeDf.loc[i, "Quantity"].split("%")[1]
                coffeDf.loc[i, "Product"] += coffeDf.loc[i, "Quantity"].split("%")[0] + "%" 
                ind = 0
                count_number = 0
                for c in temp_string:
                    if c.isdigit() and count_number == 0:
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("g")[0])
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        count_number += 1
                    ind += 1

            elif len(coffeDf.loc[i, "Quantity"].split("BTL")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("BTL")[1].split("g")[0].replace(" ", ""))

            elif len(coffeDf.loc[i, "Quantity"].split("G")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("G")[1].split("g")[0].replace(" ", ""))

            elif len(coffeDf.loc[i, "Quantity"].split("Pads")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("Pads")[1].split("g")[0].replace(" ", ""))

            else:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("g")[0].replace(" ", ""))

        except:
            print("There is a problem with '", coffeDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            coffeDf.loc[i, "Quantity"] = np.nan
    else: 
        coffeDf.loc[i, "Quantity"] = np.nan

## We drop all the rows with a na value and then we reset the indexing. 
coffeDf_grams = coffeDf.dropna()
coffeDf_grams = coffeDf_grams.reset_index(drop = True)

## Decommenting the line below it is possible to understand the quantity of rows stored.
# print(len(coffeDf_grams))

## We store the result in a csv file
with open("coffe_drinks_tea_grams.txt", "w") as csv_file:
    coffeDf_grams.to_csv(path_or_buf=csv_file)

# Extracting liters for following analysis

coffeDf = pd.read_csv("coffe_drinks_tea.txt")

for i in range(len(coffeDf)):
    print(coffeDf.loc[i, "Quantity"], "  ", type(coffeDf.loc[i, "Quantity"]))
    ## In this case we need to check for all the possibilities (ml, cl, dl and l). As usual, we applied the same structure to each
    ## of them in order to extract the highest amount of records. 
    if str(coffeDf.loc[i, "Quantity"]).endswith("ml"):
        try:
            ## We start to check the possibility to have the number of value and the quantity per item. 
            ## In this case, we just multiply the values.
            if len(coffeDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(coffeDf.loc[i, "Quantity"].split("x")[1].split("ml")[0].replace(" ", ""))/1000
                number_of_values = float(coffeDf.loc[i, "Quantity"].split("x")[0])
                coffeDf.loc[i, "Quantity"] =  float(single_value*number_of_values)
            
            ## Then, we check for the presence of just one percentage. In this case, we are going to update also the name of the product.
            elif len(coffeDf.loc[i, "Quantity"].split("%")) > 1: 
                ## As usual, we use a temporary string to store the result and make the code more readable.
                temp_string = coffeDf.loc[i, "Quantity"].split("%",1)[1]
                coffeDf.loc[i,"Product"] += coffeDf.loc[i, "Quantity"].split("%",1)[0] + "%"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("ml")[0].replace(" ", ""))/1000
                        count_digits += 1
                    ind += 1
            
            ## A common issue in cutting the strings for this category is "2 Sparkiling .... " string. We are going to extract 
            ## the string and check for the presence of the first number. In the majority of the cases it should be fine.
            ## In a larger project we should have checked out for the possibility of having more numbers.
            elif len(coffeDf.loc[i, "Quantity"].split("2Sparkling")) > 1: 
                ## As usual, we use a temporary string to store the result and make the code more readable.
                temp_string = coffeDf.loc[i, "Quantity"].split("2Sparkling",1)[1]
                coffeDf.loc[i,"Product"] += "2Sparkling"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("ml")[0].replace(" ", ""))/1000
                        count_digits += 1
                    ind += 1

            ## Another element that appears frequently is "smoothie". We extract all the rows with "smoothie" inside and we check if 
            ## we can cut the string at that point.
            elif  len(coffeDf.loc[i, "Quantity"].split("smoothie")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("smoothie",1)[1].split("ml",1)[1])/1000

            else:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("ml")[0].replace(" ", ""))/1000
        except: 
            print("There is a problem with '", coffeDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            coffeDf.loc[i, "Quantity"] = np.nan

    elif str(coffeDf.loc[i, "Quantity"]).endswith("cl"):
        try:
            if len(coffeDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(coffeDf.loc[i, "Quantity"].split("x")[1].split("cl")[0].replace(" ", ""))/100
                number_of_values = float(coffeDf.loc[i, "Quantity"].split("x")[0])
                coffeDf.loc[i, "Quantity"] =  float(single_value*number_of_values)

            elif len(coffeDf.loc[i, "Quantity"].split("%")) > 1: 
                temp_string = coffeDf.loc[i, "Quantity"].split("%",1)[1]
                coffeDf.loc[i,"Product"] += coffeDf.loc[i, "Quantity"].split("%",1)[0] + "%"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("cl")[0].replace(" ", ""))/100
                        count_digits += 1
                    ind += 1

            elif len(coffeDf.loc[i, "Quantity"].split("2Sparkling")) > 1: 
                temp_string = coffeDf.loc[i, "Quantity"].split("2Sparkling",1)[1]
                coffeDf.loc[i,"Product"] += "2Sparkling"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("cl")[0].replace(" ", ""))/100
                        count_digits += 1
                    ind += 1

            elif  len(coffeDf.loc[i, "Quantity"].split("smoothie")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("smoothie",1)[1].split("cl",1)[1])/100

            else:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("cl")[0].replace(" ", ""))/100
        except: 
            print("There is a problem with '", coffeDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            coffeDf.loc[i, "Quantity"] = np.nan

    elif str(coffeDf.loc[i, "Quantity"]).endswith("dl"):
        try:
            if len(coffeDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(coffeDf.loc[i, "Quantity"].split("x")[1].split("dl")[0].replace(" ", ""))/10
                number_of_values = float(coffeDf.loc[i, "Quantity"].split("x")[0])
                coffeDf.loc[i, "Quantity"] =  float(single_value*number_of_values)
            
            elif len(coffeDf.loc[i, "Quantity"].split("%")) > 1: 
                temp_string = coffeDf.loc[i, "Quantity"].split("%",1)[1]
                coffeDf.loc[i,"Product"] += coffeDf.loc[i, "Quantity"].split("%",1)[0] + "%"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("dl")[0].replace(" ", ""))/10
                        count_digits += 1
                    ind += 1
            
            elif len(coffeDf.loc[i, "Quantity"].split("2Sparkling")) > 1: 
                ## As usual, we use a temporary string to store the result and make the code more readable.
                temp_string = coffeDf.loc[i, "Quantity"].split("2Sparkling",1)[1]
                coffeDf.loc[i,"Product"] += "2Sparkling"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("dl")[0].replace(" ", ""))/10
                        count_digits += 1
                    ind += 1

            elif  len(coffeDf.loc[i, "Quantity"].split("smoothie")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("smoothie",1)[1].split("dl",1)[1])/10

            else:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("dl")[0].replace(" ", ""))/10
        except: 
            print("There is a problem with '", coffeDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            coffeDf.loc[i, "Quantity"] = np.nan

    elif str(coffeDf.loc[i, "Quantity"])[-1].lower() == "l" and str(coffeDf.loc[i, "Quantity"])[-2] != "m" and str(coffeDf.loc[i, "Quantity"])[-2] != "c":
        try: 
            if len(coffeDf.loc[i, "Quantity"].split("x")) > 1:
                single_value = float(coffeDf.loc[i, "Quantity"].split("x")[1].split("l")[0].replace(" ", ""))
                number_of_values = float(coffeDf.loc[i, "Quantity"].split("x")[0])
                coffeDf.loc[i, "Quantity"] =  float(single_value*number_of_values)

            elif len(coffeDf.loc[i, "Quantity"].split("%")) > 1: 
                temp_string = coffeDf.loc[i, "Quantity"].split("%",1)[1]
                coffeDf.loc[i,"Product"] += coffeDf.loc[i, "Quantity"].split("%",1)[0] + "%"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("l")[0].replace(" ", ""))
                        count_digits += 1
                    ind += 1

            elif len(coffeDf.loc[i, "Quantity"].split("2Sparkling")) > 1: 
                ## As usual, we use a temporary string to store the result and make the code more readable.
                temp_string = coffeDf.loc[i, "Quantity"].split("2Sparkling",1)[1]
                coffeDf.loc[i,"Product"] += "2Sparkling"
                ind = 0
                count_digits = 0
                for c in temp_string:
                    if c.isdigit() and count_digits==0:
                        coffeDf.loc[i, "Product"] += temp_string[:ind]
                        coffeDf.loc[i, "Quantity"] = float(temp_string[ind:].split("l")[0].replace(" ", ""))
                        count_digits += 1
                    ind += 1

            elif  len(coffeDf.loc[i, "Quantity"].split("smoothie")) > 1:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("smoothie",1)[1].split("l",1)[1])

            else:
                coffeDf.loc[i, "Quantity"] = float(coffeDf.loc[i, "Quantity"].split("l")[0].replace(" ", ""))
        except:
            print("There is a problem with '", coffeDf.loc[i, "Quantity"], "'\nThe value will be considered invalid.")
            coffeDf.loc[i, "Quantity"] = np.nan
    else: 
        coffeDf.loc[i, "Quantity"] = np.nan

## We decided to leave out all the repetitions of the same measurement units. We believe it is not possible to fix it in short time. 
## As specified also in other script, in a complete scraping project, with more time, it should be pivotal to address this issue 
## and get back values that now are eliminated


## We drop all the rows with a na value and then we reset the indexing. 
coffeDf_liter = coffeDf.dropna()
coffeDf_liter = coffeDf_liter.reset_index(drop=True)

## Decommenting the line below it is possible to check the number of records in the csv that we are going to ccreate.
# print(len(coffeDf_liter))

with open("coffe_drinks_tea_liters.txt", "w") as csv_file:
    coffeDf_liter.to_csv(path_or_buf=csv_file)