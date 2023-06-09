import pandas as pd
import numpy as np

## General case

breadDf = pd.read_csv("data/bread_and_pastries.txt")
coffeDf = pd.read_csv("data/coffe_drinks_tea.txt")
dairyDf = pd.read_csv("data/dairy_and_eggs.txt")
meatDf = pd.read_csv("data/fish_and_meat.txt")
vegetableDf = pd.read_csv("data/fruits_and_vegetables.txt")
frozenDf = pd.read_csv("data/frozen_food.txt")
pastaDf = pd.read_csv("data/pasta_and_canned.txt")
snacksDf = pd.read_csv("data/snacks_and_sweets.txt")

print(breadDf)
print(coffeDf)
print(dairyDf)
print(meatDf)
print(vegetableDf)
print(frozenDf)
print(pastaDf)
print(snacksDf)

frames = [breadDf, coffeDf, dairyDf, meatDf, vegetableDf, frozenDf, pastaDf, snacksDf]
migros_total = pd.concat(frames, ignore_index=True)
migros_total = migros_total.drop("Unnamed: 0", axis = "columns")
print(migros_total)

with open("data/migros_dataset.txt", "w") as csv_file:
    migros_total.to_csv(csv_file)
    print("CSV created")

## case with float price

for i in range(len(migros_total)):
    # print(migros_total.loc[i, "Price"])
    if migros_total.loc[i, "Price"] == "Regional Price":
        migros_total.loc[i, "Price"] = np.nan
    elif migros_total.loc[i, "Price"][-1] == "–":
        migros_total.loc[i, "Price"] = float(migros_total.loc[i, "Price"].replace("–", "00"))
    else:
        migros_total.loc[i,"Price"] = float(migros_total.loc[i, "Price"])

migros_total_float_price = migros_total.dropna()
migros_total_float_price = migros_total_float_price.reset_index(drop=True)

print(migros_total_float_price)

with open("data/migros_dataset_fp.txt", "w") as csv_file:
    migros_total_float_price.to_csv(csv_file)
    print("CSV created")

## case with grams , we extract all the record with a price that is not "Regional"

breadDf = pd.read_csv("data/bread_and_pastries_grams.txt")
coffeDf = pd.read_csv("data/coffe_drinks_tea_grams.txt")
dairyDf = pd.read_csv("data/dairy_and_eggs_grams.txt")
meatDf = pd.read_csv("data/fish_and_meat_grams.txt")
vegetableDf = pd.read_csv("data/fruits_and_vegetables_grams.txt")
frozenDf = pd.read_csv("data/frozen_food_grams.txt")
pastaDf = pd.read_csv("data/pasta_and_canned_grams.txt")
snacksDf = pd.read_csv("data/snacks_and_sweets_grams.txt")

# print(breadDf)
# print(coffeDf)
# print(dairyDf)
# print(meatDf)
# print(vegetableDf)
# print(frozenDf)
# print(pastaDf)
# print(snacksDf)

frames = [breadDf, coffeDf, dairyDf, meatDf, vegetableDf, frozenDf, pastaDf, snacksDf]
migros_total = pd.concat(frames, ignore_index=True)
migros_total = migros_total.drop("Unnamed: 0", axis = "columns")
print(migros_total)

for i in range(len(migros_total)):
    # print(migros_total.loc[i, "Price"])
    if migros_total.loc[i, "Price"] == "Regional Price":
        migros_total.loc[i, "Price"] = np.nan
    elif migros_total.loc[i, "Price"][-1] == "–":
        migros_total.loc[i, "Price"] = float(migros_total.loc[i, "Price"].replace("–", "00"))
    else:
        migros_total.loc[i,"Price"] = float(migros_total.loc[i, "Price"])

migros_total = migros_total.dropna()
migros_total = migros_total.reset_index(drop=True)
print(migros_total)

with open("data/migros_dataset_g.txt", "w") as csv_file:
    migros_total.to_csv(csv_file)
    print("CSV created")

## liter case, we extract all the record with a price that is not "Regional"

breadDf = pd.read_csv("data/bread_and_pastries_liters.txt")
coffeDf = pd.read_csv("data/coffe_drinks_tea_liters.txt")
dairyDf = pd.read_csv("data/dairy_and_eggs_liters.txt")
vegetableDf = pd.read_csv("data/fruits_and_vegetables_liters.txt")
frozenDf = pd.read_csv("data/frozen_food_liters.txt")
pastaDf = pd.read_csv("data/pasta_and_canned_liters.txt")

frames = [breadDf, coffeDf, dairyDf, vegetableDf, frozenDf, pastaDf]
migros_total = pd.concat(frames, ignore_index=True)
migros_total = migros_total.drop("Unnamed: 0", axis = "columns")
print(migros_total)


for i in range(len(migros_total)):
    # print(migros_total.loc[i, "Price"])
    if str(migros_total.loc[i, "Price"]) == "Regional Price":
        migros_total.loc[i, "Price"] = np.nan
    elif str(migros_total.loc[i, "Price"])[-1] == "–":
        migros_total.loc[i, "Price"] = float(migros_total.loc[i, "Price"].replace("–", "00"))
    else:
        migros_total.loc[i,"Price"] = float(migros_total.loc[i, "Price"])

migros_total = migros_total.dropna()
migros_total = migros_total.reset_index(drop=True)
print(migros_total)

with open("data/migros_dataset_l.txt", "w") as csv_file:
    migros_total.to_csv(csv_file)
    print("CSV created")



