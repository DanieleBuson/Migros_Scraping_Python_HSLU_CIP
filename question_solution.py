import pandas as pd
import numpy as np
############# First Question #############
Table_l = pd.read_csv("data/Table_l_Food_output.csv")
Table_g = pd.read_csv("data/Table_g_Food_output.csv")

coop_total=pd.concat([Table_g[["Price", "Product", "Producer", "Quantity", "Date"]],
                      Table_l[["Price", "Product", "Producer", "Quantity", "Date"]]], ignore_index=True)

migrosL= pd.read_csv("data/migros_dataset_l.txt")
migrosG= pd.read_csv("data/migros_dataset_g.txt")
migros_brands=list(migrosL['Producer'].unique())+list(migrosG['Producer'].unique())
coop_brands = list(Table_l['Producer'].unique())+list(Table_g['Producer'].unique())
common_brands=list(set(coop_brands) & set(migros_brands))
Migros_tot=pd.concat([migrosL[["Price", "Product", "Producer", "Quantity", "Date"]],
                     migrosG[["Price", "Product", "Producer", "Quantity", "Date"]]], ignore_index=True)

CRED = '\033[101m'
CEND = '\033[0m'
CGRE = '\33[102m'

for i in common_brands:
    sumMigros = 0
    countMigros = 0
    sumCoop = 0
    countCoop =0 
    
    for j in range(len(Migros_tot)):
        # print(Migros_tot.loc[j, "Producer"])
        if i == Migros_tot.loc[j, "Producer"]:
            sumMigros += float(Migros_tot.loc[j, "Price"])
            countMigros += 1
    
    for k in range(len(Migros_tot)):
        if i == coop_total.loc[k, "Producer"]:
            sumCoop += float(coop_total.loc[k, "Price"])
            countCoop += 1
    print("Migros", sumMigros)
    print("Coop", sumCoop)
    try:
        averageMigros = sumMigros/countMigros
        averageCoop = sumCoop/countCoop
        if averageMigros > averageCoop:
            print(CRED+'For the brand '+i+' Coop is on average more convenient than Migros'+CEND)
        else:
            print(CGRE+'For the brand '+i+' Migros is on average more convenient than Coop'+CEND)
    except Exception:
        print("\n")


############# Second Question #############

## We developed the code below in order to be able to check for keyword in different tables
## As before, we use the csv as a bridge between the extraction and pandas. Csv files makes everything faster.
## With this piece of code, we can answer several question releted to "Product category analysis".
## The user can check the products by keywords, in particular, it is possible to get information regarding average prices
## average quantity in grams and in liters, plus general information on a keyword.


## extraction of all the data from CSV and TXT from Migros (first) and Coop (second)
migros_total_float_price = pd.read_csv("data/migros_dataset_fp.txt")
migros_total_float_price.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)
migros_total_float_price = migros_total_float_price[["Price","Product","Producer","Quantity","TypeOfFood","Supermarket","Date"]]

migros_total_g = pd.read_csv("data/migros_dataset_g.txt")
migros_total_g.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)
migros_total_g = migros_total_g[["Price","Product","Producer","Quantity","TypeOfFood","Supermarket","Date"]]

migros_total_l = pd.read_csv("data/migros_dataset_l.txt")
migros_total_l.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)
migros_total_l = migros_total_l[["Price","Product","Producer","Quantity","TypeOfFood","Supermarket","Date"]]


food_coop = pd.read_csv("data/Food_output.csv")
food_coop = food_coop[["Price","Product","Producer","Quantity","TypeOfFood","Supermarket","Date"]]
food_coop_g = pd.read_csv("data/Table_g_Food_output.csv")
food_coop_g = food_coop_g[["Price","Product","Producer","Quantity","TypeOfFood","Supermarket","Date"]]
food_coop_l = pd.read_csv("data/Table_l_Food_output.csv")
food_coop_l = food_coop_l[["Price","Product","Producer","Quantity","TypeOfFood","Supermarket","Date"]]

total_float_price = pd.concat([migros_total_float_price, food_coop], ignore_index=True)
total_g = pd.concat([migros_total_g, food_coop_g], ignore_index=True)
total_l = pd.concat([migros_total_l, food_coop_l], ignore_index=True)



## We create a interactive program to search a specific keyword from different dataset (dataset with price in float,dataset with grams in float or liters in float)
cond = True
while cond:

    try:
        choice = int(input("Insert 1 for searching through the data with a regular price in CHF\n" + 
            "Insert 2 for searching through the data with price per grams" +
            "\nInsert 3 for searching through the data with price per liter" +
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
            for i in range(len(total_float_price)):
                if keyword.lower() in total_float_price.loc[i, "Product"].lower():
                    print("Product: ", total_float_price.loc[i, "Product"], "\nProducer: ", total_float_price.loc[i, "Producer"], 
                        "\nPrice: ", total_float_price.loc[i, "Price"], "\nSupermarket: ", total_float_price.loc[i, "Supermarket"], "\n")
                    count += 1
                    sum_val += total_float_price.loc[i, "Price"]
                    sum_val_squared += total_float_price.loc[i, "Price"]**2
                    if total_float_price.loc[i,"Price"] > maximum_price:
                        maximum_price = total_float_price.loc[i, "Price"]
                        maximum_product = str(total_float_price.loc[i,"Product"]) + ", price: " + str(maximum_price)
                    if total_float_price.loc[i,"Price"] < minimum_price:
                        minimum_price = total_float_price.loc[i, "Price"]
                        minimum_product = str(total_float_price.loc[i,"Product"]) + ", price: " + str(minimum_price)

            ## we display number of records, most expensive and cheapest product, average price and variance of price
            print("\nNumber of records:  ", count)
            print("\nMost expensive product:  ", maximum_product)
            print("\nCheapest product:  ", minimum_product)
            print("\nAverage price:  ", str(sum_val/count))
            print("\nPrice standard deviation:  ", str((sum_val_squared/count - (sum_val/count)**2)**0.5), "\n")

        ## if choice is 2 we check for the keyword and return the products from the dataset that have quantity in grams
        elif choice == 2:
            keyword = input("Insert Keyword: \n")
            print("\n")
            count = 0
            maximum_pricexquantity = 0
            maximum_product = ""
            minimum_pricexquantity = 100000
            minimum_product = ""
            sum_val = 0
            sum_val_squared = 0
            for i in range(len(total_g)):
                if keyword.lower() in total_g.loc[i, "Product"].lower():
                    print("Product: ", total_g.loc[i, "Product"], "\nProducer: ", total_g.loc[i, "Producer"], 
                        "\nPrice: ", total_g.loc[i, "Price"], "\nSupermarket: ", total_g.loc[i, "Supermarket"], "\n")
                    count += 1
                    sum_val += float(total_g.loc[i,"Price"])/float(total_g.loc[i,"Quantity"])
                    sum_val_squared += (float(total_g.loc[i,"Price"])/float(total_g.loc[i,"Quantity"]))**2
                    if float(total_g.loc[i,"Price"])/float(total_g.loc[i,"Quantity"]) > maximum_pricexquantity:
                        maximum_pricexquantity = float(total_g.loc[i,"Price"])/float(total_g.loc[i,"Quantity"]) 
                        maximum_product = str(total_g.loc[i,"Product"]) + ", price: " + str(maximum_pricexquantity)
                    if float(total_g.loc[i,"Price"])/float(total_g.loc[i,"Quantity"])  < minimum_pricexquantity:
                        minimum_pricexquantity = float(total_g.loc[i,"Price"])/float(total_g.loc[i,"Quantity"]) 
                        minimum_product = str(total_g.loc[i,"Product"]) + ", price: " + str(minimum_pricexquantity)

            ## we display number of records, heaviest product and lightests product, average quantity and standard deviation
            print("\n\nNumber of records:  ", count)
            print("\nMost expensive product:  ", maximum_product)
            print("\nCheapest product:  ", minimum_product)
            print("\nAverage price per gram:  ", str(sum_val/count))
            print("\nPrice per gram standard deviation:  ", str((sum_val_squared/count - (sum_val/count)**2)**0.5), "\n")

        ## if choice is 3 we check for the keyword and return the products from the dataset that have quantity in liters
        elif choice == 3:
            keyword = input("Insert Keyword: \n")
            print("\n")
            count = 0
            maximum_pricexquantity = 0
            maximum_product = ""
            minimum_pricexquantity = 100000
            minimum_product = ""
            sum_val = 0
            sum_val_squared = 0
            for i in range(len(total_l)):
                if keyword.lower() in total_l.loc[i, "Product"].lower():
                    print("Product: ", total_l.loc[i, "Product"], "\nProducer: ", total_l.loc[i, "Producer"], 
                    "\nPrice: ", total_l.loc[i, "Price"], "\nSupermarket: ", total_l.loc[i, "Supermarket"], "\n")
                    count += 1
                    sum_val += float(total_l.loc[i,"Price"])/float(total_l.loc[i,"Quantity"])
                    sum_val_squared += (float(total_l.loc[i,"Price"])/float(total_l.loc[i,"Quantity"]))**2
                    if float(total_l.loc[i,"Quantity"]) > maximum_pricexquantity:
                        maximum_pricexquantity = float(total_l.loc[i,"Price"])/float(total_l.loc[i,"Quantity"])
                        maximum_product = str(total_l.loc[i,"Product"]) + ", price per liter: " + str(maximum_pricexquantity)
                    if float(total_l.loc[i,"Quantity"]) < minimum_pricexquantity:
                        minimum_pricexquantity = float(total_l.loc[i,"Price"])/float(total_l.loc[i,"Quantity"])
                        minimum_product = str(total_l.loc[i,"Product"]) + ", price per liter: " + str(minimum_pricexquantity)
            ## we display number of records, heaviest product and lightests product, average quantity and standard deviation
            print("\n\nNumber of records:  ", count)
            print("\nMost expensive product:  ", maximum_product)
            print("\nCheapest product:  ", minimum_product)
            print("\nAverage price per liter:  ", str(sum_val/count))
            print("\Price per liter standard deviation:  ", str((sum_val_squared/count - (sum_val/count)**2)**0.5), "\n")

        ## if there is an error we catch an exception or if the choice is out of range we raise and catch an exception manually
        else: 
            raise Exception("Please, insert a digit between 0 and 4!")
    except Exception as e:
        print(e.args)
            

############# Third Question #############

## Extract the data from the CSV files
tabDf_g = pd.read_csv("data/average_prices_grams_prices.csv")
tabDf_l = pd.read_csv("data/average_prices_liters_price.csv")

CRED = '\033[101m'
CEND = '\033[0m'
CGRE = '\33[102m'

## loop through the goods in the CSV files
for j in range(len(tabDf_g)):
    # print("\n" + tabDf_g.loc[j, "item_description"] + "\n")
    ## We prepare the count to extract the average from the total data.
    total = 0
    count = 0
    average = 0
    ## we loop trhough the products
    for i in range(len(total_g)):
        ## if the keyword in tabDF is also in the product string then we extract the price per grams and we update the count
        if tabDf_g.loc[j, "item_description"].lower() in total_g.loc[i, "Product"].lower():
            total += (float(total_g.loc[i, "Price"])*1000)/float(total_g.loc[i, "Quantity"])
            count += 1
            # if float(tabDf_g.loc[j, "avg_price_chf"]) < (float(total_g.loc[i, "Price"])*1000)/float(total_g.loc[i, "Quantity"]):
            #     print(CRED + "The product " + total_g.loc[i, "Product"] + " in "+ total_g.loc[i, "Supermarket"] +" is above the average price!" + CEND)
            # else:
            #     print(CGRE + "The product " + total_g.loc[i, "Product"] + " in "+ total_g.loc[i, "Supermarket"] +" is below the average price!" + CEND)
    
    print("\n\n")
    ## we calculate the average 
    average = float(total)/float(count)
    ## We show in green if the average is below the Swiss average value, we display in red the result if the average is above the Swiss average.
    if average < float(tabDf_g.loc[j, "avg_price_chf"]):
        print(CRED + "The average price of " + tabDf_g.loc[j, "item_description"] + " is below the estimation done scraping Migros and Coop data! => Migros and Coop are more expansive" + CEND)
    else:
        print(CGRE + "The average price of " + tabDf_g.loc[j, "item_description"] + " is above or in line with the estimation done scraping Migros and Coop data! => Migros and Coop are in line with prices" + CEND)
    print("\n\n") 


## We do the same for liters.
for j in range(len(tabDf_l)):
    print("\n" + tabDf_l.loc[j, "item_description"] + "\n")
    total = 0
    count = 0
    average = 0
    for i in range(len(total_l)):

        if tabDf_l.loc[j, "item_description"].lower() in total_l.loc[i, "Product"].lower():
            total += (float(total_l.loc[i, "Price"]))/float(total_l.loc[i, "Quantity"])
            count += 1
            # if float(tabDf_l.loc[j, "avg_price_chf"]) < (float(total_l.loc[i, "Price"]))/float(total_l.loc[i, "Quantity"]):
            #     print(CRED + "The product " + total_l.loc[i, "Product"] + " in "+ total_l.loc[i, "Supermarket"] +" is above the average price!" + CEND)
            # else:
            #     print(CGRE + "The product " + total_l.loc[i, "Product"] + " in "+ total_l.loc[i, "Supermarket"] +" is below the average price!" + CEND)
    
    print("\n\n")
    average = float(total)/float(count)
    if average < float(tabDf_l.loc[j, "avg_price_chf"]):
        print(CRED + "The average price of " + tabDf_l.loc[j, "item_description"] + " is below the estimation done scraping Migros and Coop data! => Migros and Coop are more expansive" + CEND)
    else:
        print(CGRE + "The average price of " + tabDf_l.loc[j, "item_description"] + " is above or in line with the estimation done scraping Migros and Coop data! => Migros and Coop are in line with prices" + CEND)
    print("\n\n") 
