import pandas as pd
import mariadb
import sys

try: con = mariadb.connect( 

    user="daniele", 

    password="mypass", 

    host="localhost", 

    port=3306, 

    database="grocery" 

)

except mariadb.Error as ex: 

    print(f"An error occurred while connecting to MariaDB: {ex}") 

    sys.exit(1) 

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Fruits_and_Vegetables_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")
cur.execute("CREATE TABLE IF NOT EXISTS Fruits_and_Vegetables_liters (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")

cur.execute("CREATE TABLE IF NOT EXISTS Meat_and_Fish_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")

cur.execute("CREATE TABLE IF NOT EXISTS Bread_and_Pastries_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")
cur.execute("CREATE TABLE IF NOT EXISTS Bread_and_Pastries_liters (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")

cur.execute("CREATE TABLE IF NOT EXISTS Coffe_Drinks_Tea_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")
cur.execute("CREATE TABLE IF NOT EXISTS Coffe_Drinks_Tea_liters (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")


cur.execute("CREATE TABLE IF NOT EXISTS Dairy_and_Eggs_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")
cur.execute("CREATE TABLE IF NOT EXISTS Dairy_and_Eggs_liters (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")


cur.execute("CREATE TABLE IF NOT EXISTS Frozen_Food_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")
cur.execute("CREATE TABLE IF NOT EXISTS Frozen_Food_liters (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")


cur.execute("CREATE TABLE IF NOT EXISTS Pasta_and_Canned_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")
cur.execute("CREATE TABLE IF NOT EXISTS Pasta_and_Canned_liters (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")


cur.execute("CREATE TABLE IF NOT EXISTS Snacks_grams (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Price FLOAT, Product VARCHAR(255), Producer VARCHAR(255), Quantity FLOAT, TypeOfFood VARCHAR(255), Supermarket VARCHAR(255), Date DATE, PRIMARY KEY (ProductId));")


cur.execute("SHOW TABLES;")
res = cur.fetchall()
print(res)

##############################################
############# BREAD AND PASTRIES #############
##############################################

breadDf = pd.read_csv("data/bread_and_pastries_grams.txt")
breadDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
breadDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(breadDf)

for i in range(len(breadDf)):
    # print(breadDf.loc[i, "Price"])
    if breadDf.loc[i, "Price"] == "Regional Price":
        breadDf.loc[i, "Price"] = "NULL"
    elif str(breadDf.loc[i, "Price"])[-1] == "–":
        breadDf.loc[i, "Price"] = float(breadDf.loc[i, "Price"].replace("–", "00"))
    else:
        breadDf.loc[i,"Price"] = float(breadDf.loc[i, "Price"])



for i in range(len(breadDf)):
    sql_insert = "INSERT INTO Bread_and_Pastries_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    breadDf.loc[i,"Price"],
    breadDf.loc[i,"Product"], 
    breadDf.loc[i,"Producer"], 
    float(breadDf.loc[i,"Quantity"]), 
    breadDf.loc[i,"TypeOfFood"], 
    breadDf.loc[i,"Supermarket"], 
    breadDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Bread_and_Pastries_grams;")

print(cur.fetchall())

breadDf = pd.read_csv("data/bread_and_pastries_liters.txt")
breadDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
breadDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(breadDf)

for i in range(len(breadDf)):
    # print(breadDf.loc[i, "Price"])
    if breadDf.loc[i, "Price"] == "Regional Price":
        breadDf.loc[i, "Price"] = "NULL"
    elif str(breadDf.loc[i, "Price"])[-1] == "–":
        breadDf.loc[i, "Price"] = float(breadDf.loc[i, "Price"].replace("–", "00"))
    else:
        breadDf.loc[i,"Price"] = float(breadDf.loc[i, "Price"])



for i in range(len(breadDf)):
    sql_insert = "INSERT INTO Bread_and_Pastries_liters (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    breadDf.loc[i,"Price"],
    breadDf.loc[i,"Product"], 
    breadDf.loc[i,"Producer"], 
    float(breadDf.loc[i,"Quantity"]), 
    breadDf.loc[i,"TypeOfFood"], 
    breadDf.loc[i,"Supermarket"], 
    breadDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Bread_and_Pastries_liters;")

print(cur.fetchall())

################################################
############# COFFE DRINKS AND TEA #############
################################################

coffeDF = pd.read_csv("data/coffe_drinks_tea_grams.txt")
coffeDF.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
coffeDF.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(coffeDF)

for i in range(len(coffeDF)):
    # print(breadDf.loc[i, "Price"])
    if coffeDF.loc[i, "Price"] == "Regional Price":
        coffeDF.loc[i, "Price"] = "NULL"
    elif str(coffeDF.loc[i, "Price"])[-1] == "–":
        coffeDF.loc[i, "Price"] = float(coffeDF.loc[i, "Price"].replace("–", "00"))
    else:
        coffeDF.loc[i,"Price"] = float(coffeDF.loc[i, "Price"])



for i in range(len(coffeDF)):
    sql_insert = "INSERT INTO Coffe_Drinks_Tea_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    coffeDF.loc[i,"Price"],
    coffeDF.loc[i,"Product"], 
    coffeDF.loc[i,"Producer"], 
    float(coffeDF.loc[i,"Quantity"]), 
    coffeDF.loc[i,"TypeOfFood"], 
    coffeDF.loc[i,"Supermarket"], 
    coffeDF.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Coffe_Drinks_Tea_grams;")

print(cur.fetchall())

coffeDF = pd.read_csv("data/coffe_drinks_tea_liters.txt")
coffeDF.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
coffeDF.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(coffeDF)

for i in range(len(coffeDF)):
    # print(breadDf.loc[i, "Price"])
    if coffeDF.loc[i, "Price"] == "Regional Price":
        coffeDF.loc[i, "Price"] = "NULL"
    elif str(coffeDF.loc[i, "Price"])[-1] == "–":
        coffeDF.loc[i, "Price"] = float(coffeDF.loc[i, "Price"].replace("–", "00"))
    else:
        coffeDF.loc[i,"Price"] = float(coffeDF.loc[i, "Price"])



for i in range(len(coffeDF)):
    sql_insert = "INSERT INTO Coffe_Drinks_Tea_liters (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    coffeDF.loc[i,"Price"],
    coffeDF.loc[i,"Product"], 
    coffeDF.loc[i,"Producer"], 
    float(coffeDF.loc[i,"Quantity"]), 
    coffeDF.loc[i,"TypeOfFood"], 
    coffeDF.loc[i,"Supermarket"], 
    coffeDF.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Coffe_Drinks_Tea_liters;")

print(cur.fetchall())

##########################################
############# DAIRY PRODUCTS #############
##########################################

dairyDf = pd.read_csv("data/dairy_and_eggs_grams.txt")
dairyDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
dairyDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(dairyDf)

for i in range(len(dairyDf)):
    # print(breadDf.loc[i, "Price"])
    if dairyDf.loc[i, "Price"] == "Regional Price":
        dairyDf.loc[i, "Price"] = "NULL"
    elif str(dairyDf.loc[i, "Price"])[-1] == "–":
        dairyDf.loc[i, "Price"] = float(dairyDf.loc[i, "Price"].replace("–", "00"))
    else:
        dairyDf.loc[i,"Price"] = float(dairyDf.loc[i, "Price"])



for i in range(len(dairyDf)):
    sql_insert = "INSERT INTO Dairy_and_Eggs_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    dairyDf.loc[i,"Price"],
    dairyDf.loc[i,"Product"], 
    dairyDf.loc[i,"Producer"], 
    float(dairyDf.loc[i,"Quantity"]), 
    dairyDf.loc[i,"TypeOfFood"], 
    dairyDf.loc[i,"Supermarket"], 
    dairyDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Dairy_and_Eggs_grams;")

print(cur.fetchall())


dairyDf = pd.read_csv("data/dairy_and_eggs_liters.txt")
dairyDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
dairyDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(dairyDf)

for i in range(len(dairyDf)):
    # print(breadDf.loc[i, "Price"])
    if dairyDf.loc[i, "Price"] == "Regional Price":
        dairyDf.loc[i, "Price"] = "NULL"
    elif str(dairyDf.loc[i, "Price"])[-1] == "–":
        dairyDf.loc[i, "Price"] = float(dairyDf.loc[i, "Price"].replace("–", "00"))
    else:
        dairyDf.loc[i,"Price"] = float(dairyDf.loc[i, "Price"])



for i in range(len(dairyDf)):
    sql_insert = "INSERT INTO Dairy_and_Eggs_liters (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    dairyDf.loc[i,"Price"],
    dairyDf.loc[i,"Product"], 
    dairyDf.loc[i,"Producer"], 
    float(dairyDf.loc[i,"Quantity"]), 
    dairyDf.loc[i,"TypeOfFood"], 
    dairyDf.loc[i,"Supermarket"], 
    dairyDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Dairy_and_Eggs_liters;")

print(cur.fetchall())

#########################################
############# FISH AND MEAT #############
#########################################

meatDf = pd.read_csv("data/fish_and_meat_grams.txt")
meatDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
meatDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(meatDf)

for i in range(len(meatDf)):
    # print(breadDf.loc[i, "Price"])
    if meatDf.loc[i, "Price"] == "Regional Price":
        meatDf.loc[i, "Price"] = "NULL"
    elif str(meatDf.loc[i, "Price"])[-1] == "–":
        meatDf.loc[i, "Price"] = float(meatDf.loc[i, "Price"].replace("–", "00"))
    else:
        meatDf.loc[i,"Price"] = float(meatDf.loc[i, "Price"])



for i in range(len(meatDf)):
    sql_insert = "INSERT INTO Meat_and_Fish_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    meatDf.loc[i,"Price"],
    meatDf.loc[i,"Product"], 
    meatDf.loc[i,"Producer"], 
    float(meatDf.loc[i,"Quantity"]), 
    meatDf.loc[i,"TypeOfFood"], 
    meatDf.loc[i,"Supermarket"], 
    meatDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Meat_and_Fish_grams;")

print(cur.fetchall())

#######################################
############# FROZEN FOOD #############
#######################################

frozenDf = pd.read_csv("data/frozen_food_grams.txt")
frozenDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
frozenDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(frozenDf)

for i in range(len(frozenDf)):
    # print(breadDf.loc[i, "Price"])
    if frozenDf.loc[i, "Price"] == "Regional Price":
        frozenDf.loc[i, "Price"] = "NULL"
    elif str(frozenDf.loc[i, "Price"])[-1] == "–":
        frozenDf.loc[i, "Price"] = float(frozenDf.loc[i, "Price"].replace("–", "00"))
    else:
        frozenDf.loc[i,"Price"] = float(frozenDf.loc[i, "Price"])



for i in range(len(frozenDf)):
    sql_insert = "INSERT INTO Frozen_Food_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    frozenDf.loc[i,"Price"],
    frozenDf.loc[i,"Product"], 
    frozenDf.loc[i,"Producer"], 
    float(frozenDf.loc[i,"Quantity"]), 
    frozenDf.loc[i,"TypeOfFood"], 
    frozenDf.loc[i,"Supermarket"], 
    frozenDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Frozen_Food_grams;")

print(cur.fetchall())

frozenDf = pd.read_csv("data/frozen_food_liters.txt")
frozenDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
frozenDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(frozenDf)

for i in range(len(frozenDf)):
    # print(breadDf.loc[i, "Price"])
    if frozenDf.loc[i, "Price"] == "Regional Price":
        frozenDf.loc[i, "Price"] = "NULL"
    elif str(frozenDf.loc[i, "Price"])[-1] == "–":
        frozenDf.loc[i, "Price"] = float(frozenDf.loc[i, "Price"].replace("–", "00"))
    else:
        frozenDf.loc[i,"Price"] = float(frozenDf.loc[i, "Price"])



for i in range(len(frozenDf)):
    sql_insert = "INSERT INTO Frozen_Food_liters (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    frozenDf.loc[i,"Price"],
    frozenDf.loc[i,"Product"], 
    frozenDf.loc[i,"Producer"], 
    float(frozenDf.loc[i,"Quantity"]), 
    frozenDf.loc[i,"TypeOfFood"], 
    frozenDf.loc[i,"Supermarket"], 
    frozenDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Frozen_Food_liters;")

print(cur.fetchall())

#################################################
############# FRUITS AND VEGETABLES #############
#################################################

vegDf = pd.read_csv("data/fruits_and_vegetables_grams.txt")
vegDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
vegDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(vegDf)

for i in range(len(vegDf)):
    # print(breadDf.loc[i, "Price"])
    if vegDf.loc[i, "Price"] == "Regional Price":
        vegDf.loc[i, "Price"] = "NULL"
    elif str(vegDf.loc[i, "Price"])[-1] == "–":
        vegDf.loc[i, "Price"] = float(vegDf.loc[i, "Price"].replace("–", "00"))
    else:
        vegDf.loc[i,"Price"] = float(vegDf.loc[i, "Price"])



for i in range(len(vegDf)):
    sql_insert = "INSERT INTO Fruits_and_Vegetables_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    vegDf.loc[i,"Price"],
    vegDf.loc[i,"Product"], 
    vegDf.loc[i,"Producer"], 
    float(vegDf.loc[i,"Quantity"]), 
    vegDf.loc[i,"TypeOfFood"], 
    vegDf.loc[i,"Supermarket"], 
    vegDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Fruits_and_Vegetables_grams;")

print(cur.fetchall())

vegDf = pd.read_csv("data/fruits_and_vegetables_liters.txt")
vegDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
vegDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(vegDf)

for i in range(len(vegDf)):
    # print(breadDf.loc[i, "Price"])
    if vegDf.loc[i, "Price"] == "Regional Price":
        vegDf.loc[i, "Price"] = "NULL"
    elif str(vegDf.loc[i, "Price"])[-1] == "–":
        vegDf.loc[i, "Price"] = float(vegDf.loc[i, "Price"].replace("–", "00"))
    else:
        vegDf.loc[i,"Price"] = float(vegDf.loc[i, "Price"])



for i in range(len(vegDf)):
    sql_insert = "INSERT INTO Fruits_and_Vegetables_liters (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    vegDf.loc[i,"Price"],
    vegDf.loc[i,"Product"], 
    vegDf.loc[i,"Producer"], 
    float(vegDf.loc[i,"Quantity"]), 
    vegDf.loc[i,"TypeOfFood"], 
    vegDf.loc[i,"Supermarket"], 
    vegDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Fruits_and_Vegetables_liters;")

print(cur.fetchall())

#################################################
############# PASTA AND CANNED FOOD #############
#################################################

pastaDf = pd.read_csv("data/pasta_and_canned_grams.txt")
pastaDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
pastaDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(pastaDf)

for i in range(len(pastaDf)):
    # print(breadDf.loc[i, "Price"])
    if pastaDf.loc[i, "Price"] == "Regional Price":
        pastaDf.loc[i, "Price"] = "NULL"
    elif str(pastaDf.loc[i, "Price"])[-1] == "–":
        pastaDf.loc[i, "Price"] = float(pastaDf.loc[i, "Price"].replace("–", "00"))
    else:
        pastaDf.loc[i,"Price"] = float(pastaDf.loc[i, "Price"])



for i in range(len(pastaDf)):
    sql_insert = "INSERT INTO Pasta_and_Canned_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    pastaDf.loc[i,"Price"],
    pastaDf.loc[i,"Product"], 
    pastaDf.loc[i,"Producer"], 
    float(pastaDf.loc[i,"Quantity"]), 
    pastaDf.loc[i,"TypeOfFood"], 
    pastaDf.loc[i,"Supermarket"], 
    pastaDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Pasta_and_Canned_grams;")

print(cur.fetchall())

pastaDf = pd.read_csv("data/pasta_and_canned_liters.txt")
pastaDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
pastaDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(pastaDf)

for i in range(len(pastaDf)):
    # print(breadDf.loc[i, "Price"])
    if pastaDf.loc[i, "Price"] == "Regional Price":
        pastaDf.loc[i, "Price"] = "NULL"
    elif str(pastaDf.loc[i, "Price"])[-1] == "–":
        pastaDf.loc[i, "Price"] = float(pastaDf.loc[i, "Price"].replace("–", "00"))
    else:
        pastaDf.loc[i,"Price"] = float(pastaDf.loc[i, "Price"])



for i in range(len(pastaDf)):
    sql_insert = "INSERT INTO Pasta_and_Canned_liters (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    pastaDf.loc[i,"Price"],
    pastaDf.loc[i,"Product"], 
    pastaDf.loc[i,"Producer"], 
    float(pastaDf.loc[i,"Quantity"]), 
    pastaDf.loc[i,"TypeOfFood"], 
    pastaDf.loc[i,"Supermarket"], 
    pastaDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Pasta_and_Canned_liters;")

print(cur.fetchall())

#############################################
############# SNACKS AND SWEETS #############
#############################################

snacksDf = pd.read_csv("data/snacks_and_sweets_grams.txt")
snacksDf.rename(columns={"Unnamed: 0" : "ProductId"}, inplace=True)
snacksDf.rename(columns={"Type of food": "TypeOfFood"}, inplace=True)

print(snacksDf)

for i in range(len(snacksDf)):
    # print(breadDf.loc[i, "Price"])
    if snacksDf.loc[i, "Price"] == "Regional Price":
        snacksDf.loc[i, "Price"] = "NULL"
    elif str(snacksDf.loc[i, "Price"])[-1] == "–":
        snacksDf.loc[i, "Price"] = float(snacksDf.loc[i, "Price"].replace("–", "00"))
    else:
        snacksDf.loc[i,"Price"] = float(snacksDf.loc[i, "Price"])



for i in range(len(snacksDf)):
    sql_insert = "INSERT INTO Snacks_grams (Price, Product, Producer, Quantity, TypeOfFood, Supermarket, Date) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\");".format(
    snacksDf.loc[i,"Price"],
    snacksDf.loc[i,"Product"], 
    snacksDf.loc[i,"Producer"], 
    float(snacksDf.loc[i,"Quantity"]), 
    snacksDf.loc[i,"TypeOfFood"], 
    snacksDf.loc[i,"Supermarket"], 
    snacksDf.loc[i,"Date"])
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Snacks_grams;")

print(cur.fetchall())

