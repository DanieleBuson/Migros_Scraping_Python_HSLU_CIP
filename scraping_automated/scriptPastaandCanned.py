from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import pandas as pd

# comment -> line commented due to coding resons 
## comment -> comment for the reader of the code, these comments provide the reasons and motivations behind each line of code.

obj = datetime.now()

url = 'https://www.migros.ch/en/category/pasta-condiments-canned-food'

## In this case we decided to use Chrome as a web browser, using the selenium command webdriver.Chrome(). However, it is possible to set a different browser (Firefox, Edge...)
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(10)
page = driver.page_source
driver.quit()
## We pass the page extracted using selenium to BeutifulSoup in order to extract data through the html. 
soup = BeautifulSoup(page, 'html.parser')

brands=[]
## We extract the brands that can be used in the next step
## In order to do that, we search for the HTML component ("label")
for element in soup.select("label"):
    ## We initialised the index to 0 
    ind = 0
    for char in element.get_text():
        ## We found out that the charcater "(". 
        if char == "(":
            ind +=1
    ## If there is only one character, it means we can extract the brand using the method split
    if ind == 1:
        brands.append(element.get_text().split("(")[0].replace(" ", ""))

## We just add the space between the words (in case they are two) in the brand's names to create a smoother process later.
for j in range(len(brands)):
    element = brands[j]
    count = 0
    i = 0
    for c in element:
        if c.isupper():
            count += 1
            if count == 2: 
                temp1 = element[:i]
                temp2 = element[i:]
                brands[j] = temp1 + " " + temp2
                print(brands[i])
        i += 1

print(str(brands))



url = 'https://www.migros.ch/en/category/pasta-condiments-canned-food'

## In this case we decided to use Chrome as a web browser, using the selenium command webdriver.Chrome(). However, it is possible to set a different browser (Firefox, Edge...)
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(70)
page = driver.page_source
driver.quit()
## We pass the page extracted using selenium to BeutifulSoup in order to extract data through the html. 
soup = BeautifulSoup(page, 'html.parser')

vegetables = []
for element in soup.select("li"):
    ## This step was thought carefully after looking at the output of soup.select("li").
    ## We are going to store the result inside of a list only if respect a certain starting condition.
    if (element.get_text()[0].isdigit() or element.get_text()[1].isdigit() or element.get_text()[2].isdigit() or element.get_text().startswith(" Regional")):
        vegetables.append(element.get_text())

prices = []
producer = []
product = []
quantity = []
ToF = []
supermarket = []
date = []
row = 0
for element in vegetables:
    ## There are three possibilities, discounted, normally priced and regional regulated priced food. The first category
    ## will not be considered, since it is too complicated to consider discounts on the analysis. 
    ## Fro what concerns the second category it is quite straighforward how to divide them through splitting teh strings. 
    if element.split(" ")[0] == "":
        # Regular prices data extraction. We check if the keyword is Regional. In that case we proceed with the analysis
        if element.split(" ")[1] != "Regional":
            price = element.split(" ")[1]
            tempString = element.split(" ",2)[2].split("\n")[0]
            print(tempString)
            ind = 0
            for brand in brands:
                if tempString.startswith(brand):
                    ind += 1
                    tempString = tempString.split(brand, 1)[1]
                    # print(tempString)
                    i = 0
                    count_digit = 0
                    for char in tempString:
                        if char.isdigit() and count_digit==0:
                            prices.append(price)
                            producer.append(brand.replace('"', ' '))
                            product.append(tempString[0:i].replace('"', ' '))
                            quantity.append(tempString[i:].replace('"', ' '))
                            ToF.append("Pasta, Condiments & Canned Food")
                            date.append(obj.strftime("%Y-%m-%d"))
                            supermarket.append("Migros")
                            count_digit += 1
                            # print(prices[row], "  ", producer[row], "   ", product[row])
                        i+=1
            if ind == 0:
                i = 0
                count_digit = 0
                for char in tempString:
                    if char.isdigit() and count_digit == 0:
                        prices.append(price)
                        producer.append("unknown")
                        product.append(tempString[0:i])
                        quantity.append(tempString[i:])
                        ToF.append("Pasta, Condiments & Canned Food")
                        date.append(obj.strftime("%Y-%m-%d")) 
                        supermarket.append("Migros")
                        count_digit += 1
                    i += 1
                # print(price, "  ", "unknown  ", tempString)
        else:
            tempString = element.split(" ",2)[2].split("\n")[1]
            ind = 0
            for brand in brands:
                if tempString.startswith(brand):
                    ind += 1
                    prices.append("Regional Price")
                    producer.append(brand)
                    product.append(tempString.split(brand, 1)[1])
                    quantity.append("NA")
                    ToF.append("Pasta, Condiments & Canned Food")
                    supermarket.append("Migros")
                    date.append(obj.strftime("%Y-%m-%d"))
                    # print("regional price", " ", brand, tempString.split(brand, 1)[1])
            if ind == 0:
                prices.append("Regional Price")
                producer.append("unknown")
                product.append(tempString)
                quantity.append("NA")
                ToF.append("Pasta, Condiments & Canned Food")
                supermarket.append("Migros")
                date.append(obj.strftime("%Y-%m-%d"))
                # print("Regional price  unknown  ", tempString)
    # row += 1

print(len(prices))
print(len(producer))
print(len(product))

## After the loop, I decided to collect the result into a single list and then transform this list into a pandas data frame using the following 
## commands: 
total_list = [prices, product, producer, quantity, ToF, supermarket, date]
pastaDF = pd.DataFrame(total_list).transpose()
pastaDF.columns = ["Price", "Product", "Producer", "Quantity", "Type of food", "Supermarket", "Date"]
## Here it is the result in a tabular form.
print(pastaDF)

with open('data/pasta_and_canned.txt', 'w') as csv_file:
    pastaDF.to_csv(path_or_buf=csv_file)
