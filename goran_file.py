# Import necessary libraries: BeautifulSoup for parsing HTML, Selenium for browser automation,
# time for pausing script execution, datetime for timestamping, and pandas for data manipulation and saving.

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import pandas as pd

# comment -> line commented due to coding resons
## comment -> comment for the reader of the code, these comments provide the reasons and motivations behind each line of code.

# Store current date and time in obj. This might be used later to timestamp the data.
obj = datetime.now()

# Define the URL of the webpage to be scraped.
url = 'http://hikersbay.com/prices/switzerland?lang=en'

## In this case we decided to use Chrome as a web browser, using the selenium command webdriver.Chrome(). However, it is possible to set a different browser (Firefox, Edge...)
# Initialize the webdriver.
driver = webdriver.Chrome()

# Open the webpage at the given URL in the automated browser.
driver.get(url)

# Maximize the browser window to ensure all elements of the webpage are visible.
driver.maximize_window()

# Allow the webpage to load completely by pausing the script for 1 second.
time.sleep(1)

# Get the source HTML of the webpage.
page = driver.page_source

# Close the automated browser after page source has been captured.
driver.quit()


## We pass the page extracted using selenium to BeutifulSoup in order to extract data through the html.

# Parse the HTML page source using BeautifulSoup.
soup = BeautifulSoup(page, 'html.parser')

# Initialize an empty list to store the data extracted from the table.
test = []

# Extract each table from the HTML, check if it starts with "Price of", and if so, append its text to the 'test' list.
for element in soup.select("table"):
    if element.get_text().startswith("\n\n\nPrice of"):
        test.append(element.get_text())

# The first table (if found) in the list is then split into separate strings for each item using the newline character. The first element is removed as it is empty.
test = test[0].split("\n\n\n")[1:]

# Print the 'test' list for debugging purposes, to ensure the data was split correctly.
print(str(test))

# Initialize lists to store the item descriptions and prices in different currencies.
item_descriptions = []
prices_chf = []
prices_usd = []
prices_euro = []

# Loop through the 'test' list. Each element is split into description and prices.
# The description and prices are then appended to their respective lists.
for element in test:
    # Split the line on newline characters
    temp = element.split("\n")
    # If the line has at least 4 elements (item description and 3 price values)
    if len(temp) >= 4:  # check if temp has at least 4 elements
        # take only the item
        item = temp[0].split('Price of ')[1].split(' in Switzerland')[0]

        # Extract and convert the price values to floats
        item_descriptions.append(item)
        prices_chf.append(float(temp[1].split(" ")[0]))
        prices_usd.append(float(temp[2].split(" ")[0]))
        prices_euro.append(float(temp[3].split(" ")[0]))
    else:
        # If the line doesn't have at least 4 elements, skip it and print a message
        print(f"Skipping element: {element}")


# Lists are combined into a pandas DataFrame for easy manipulation and storage.
columns = [item_descriptions, prices_chf, prices_usd, prices_euro]
tabDF = pd.DataFrame(columns).transpose()
tabDF.columns = ["item_description", "price_chf", "price_usd", "price_euro"]

# The DataFrame is printed to the console for checking the final output.
print(tabDF)

with open("average_prices_switzerland.txt", "w") as csv_file: 
    tabDF.to_csv(csv_file)