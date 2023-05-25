import pandas as pd
import mariadb
import sys

try: con = mariadb.connect( 

    user="goran", 

    password="mypass", 

    host="localhost", 

    port=3306, 

    database="grocery" 

)

except mariadb.Error as ex: 

    print(f"An error occurred while connecting to MariaDB: {ex}") 

    sys.exit(1) 

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Average_prices (ProductId MEDIUMINT NOT NULL AUTO_INCREMENT, Item_description VARCHAR(255), PriceCHF FLOAT, PriceUSD FLOAT, PriceEuro FLOAT, PRIMARY KEY (ProductId));")

cur.execute("SHOW TABLES;")
res = cur.fetchall()
print(res)

tabDF = pd.read_csv("data/average_prices_switzerland.txt")

for i in range(len(tabDF)):
    sql_insert = "INSERT INTO Average_prices (Item_description, PriceCHF, PriceUSD, PriceEuro) VALUES (\"{}\", {}, {}, {});".format(
    tabDF.loc[i,"item_description"],
    tabDF.loc[i,"price_chf"], 
    tabDF.loc[i,"price_usd"], 
    float(tabDF.loc[i,"price_euro"]))
    # print(sql_insert)
    cur.execute(sql_insert)

con.commit()

cur.execute("SELECT * FROM Average_prices;")

print(cur.fetchall())