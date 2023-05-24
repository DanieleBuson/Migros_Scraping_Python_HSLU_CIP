import pandas as pd
import numpy as np
############# First Question #############


############# Second Question #############

## We developed the code below in order to be able to check for keyword in different tables
## As before, we use the csv as a bridge between the extraction and pandas. Csv files makes everything faster.
## With this piece of code, we can answer several question releted to "Product category analysis".
## The user can check the products by keywords, in particular, it is possible to get information regarding average prices
## average quantity in grams and in liters, plus general information on a keyword.


## extraction of all the data from CSV 
migros_total_float_price = pd.read_csv("migros_dataset_fp.txt")
migros_total = pd.read_csv("migros_dataset.txt")
migros_total_g = pd.read_csv("migros_dataset_g.txt")
migros_total_l = pd.read_csv("migros_dataset_l.txt")

## We create a interactive program to search a specific keyword from different dataset (dataset with price in float,dataset with grams in float or liters in float)
cond = True
while cond:

    try:
        choice = int(input("Insert 1 for searching through the data with a regular price in CHF\nInsert 2 for searching through the data that have quantity in grams" +
            "\nInsert 3 for searching through the data that have quantity in liters\nInsert 4 for searching though all the data" +
            "\nInsert 0 to exit.\n") )
        ## if choice is 0 the program is closed.
        if choice == 0:
            cond = False
        ## if choice is 1 we ask for the keyword and we give back the result for the search
        elif choice == 1:
            keyword = input("Insert Keyword: \n")
            print("\n")
            count = 0
            maximum_price = 0
            maximum_product = ""
            minimum_price = 1000
            minimum_product = ""
            sum_val = 0
            sum_val_squared = 0
            for i in range(len(migros_total_float_price)):
                if keyword.lower() in migros_total_float_price.loc[i, "Product"].lower():
                    print(migros_total_float_price.loc[i,])
                    count += 1
                    sum_val += migros_total_float_price.loc[i, "Price"]
                    sum_val_squared += migros_total_float_price.loc[i, "Price"]**2
                    if migros_total_float_price.loc[i,"Price"] > maximum_price:
                        maximum_product = str(migros_total_float_price.loc[i,])
                        maximum_price = migros_total_float_price.loc[i, "Price"]
                    if migros_total_float_price.loc[i,"Price"] < minimum_price:
                        minimum_product = str(migros_total_float_price.loc[i,])
                        minimum_price = migros_total_float_price.loc[i, "Price"]
            ## we display number of records, most expensive and cheapest product, average price and variance of price
            print("\nNumber of records:  ", count)
            print("\nMost expensive product:  ", maximum_product)
            print("\nCheapest product:  ", minimum_product)
            print("\nAverage price:  ", str(sum_val/count))
            print("\nPrice variance:  ", str(sum_val_squared/count - (sum_val/count)**2))
        ## if choice is 2 we check for the keyword and return the products from the dataset that have quantity in grams
        elif choice == 2:
            keyword = input("Insert Keyword: \n")
            print("\n")
            count = 0
            maximum_quantity = 0
            maximum_product = ""
            minimum_quantity = 100000
            minimum_product = ""
            sum_val = 0
            sum_val_squared = 0
            for i in range(len(migros_total_g)):
                if keyword.lower() in migros_total_g.loc[i, "Product"].lower():
                    print(migros_total_g.loc[i,])
                    count += 1
                    sum_val += migros_total_g.loc[i, "Quantity"]
                    sum_val_squared += migros_total_g.loc[i, "Quantity"]**2
                    if float(migros_total_g.loc[i,"Quantity"]) > maximum_quantity:
                        maximum_product = str(migros_total_g.loc[i,])
                        maximum_quantity = float(migros_total_g.loc[i,"Quantity"])
                    if float(migros_total_g.loc[i,"Quantity"]) < minimum_quantity:
                        minimum_product = str(migros_total_g.loc[i,])
                        minimum_quantity = float(migros_total_g.loc[i,"Quantity"])
            ## we display number of records, heaviest product and lightests product, average quantity and standard deviation
            print("\nNumber of records:  ", count)
            print("\nHeaviest product:  ", maximum_product)
            print("\nLightest product:  ", minimum_product)
            print("\nAverage quantity in grams:  ", str(sum_val/count))
            print("\nQuantity standard deviation in grams:  ", str((sum_val_squared/count - (sum_val/count)**2)**0.5))
        ## if choice is 3 we check for the keyword and return the products from the dataset that have quantity in liters
        elif choice == 3:
            keyword = input("Insert Keyword: \n")
            print("\n")
            count = 0
            maximum_quantity = 0
            maximum_product = ""
            minimum_quantity = 100000
            minimum_product = ""
            sum_val = 0
            sum_val_squared = 0
            for i in range(len(migros_total_l)):
                if keyword.lower() in migros_total_l.loc[i, "Product"].lower():
                    print(migros_total_l.loc[i,])
                    count += 1
                    sum_val += migros_total_l.loc[i, "Quantity"]
                    sum_val_squared += migros_total_l.loc[i, "Quantity"]**2
                    if float(migros_total_g.loc[i,"Quantity"]) > maximum_quantity:
                        maximum_product = str(migros_total_g.loc[i,])
                        maximum_quantity = float(migros_total_g.loc[i,"Quantity"])
                    if float(migros_total_g.loc[i,"Quantity"]) < minimum_quantity:
                        minimum_product = str(migros_total_g.loc[i,])
                        minimum_quantity = float(migros_total_g.loc[i,"Quantity"])
            ## we display number of records, heaviest product and lightests product, average quantity and standard deviation
            print("\nNumber of records:  ", count)
            print("\Maximum liters product:  ", maximum_product)
            print("\nMinimum liters product:  ", minimum_product)
            print("\nAverage quantity in liters:  ", str(sum_val/count))
            print("\nQuantity standard deviation in liters:  ", str((sum_val_squared/count - (sum_val/count)**2)**0.5))
        ## if choice is 4 we check in the general dataset
        elif choice == 4:
            keyword = input("Insert Keyword: \n")
            print("\n")
            count = 0
            for i in range(len(migros_total)):
                if keyword.lower() in str(migros_total.loc[i, "Product"]).lower():
                    count += 1
                    print(migros_total.loc[i,])
                    print("\n")
            ## We can show only the number of records since the dataset contains just strings.
            print("\nNumber of records:  ", count)
        ## if there is an error we catch an exception or if the choice is out of range we raise and catch an exception manually
        else: 
            raise Exception("Please, insert a digit between 0 and 4!")
    except Exception as e:
        print(e.args)
            

############# Third Question #############