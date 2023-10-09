# Migros Data Scraping and Analysis

## Introduction
This document provides instructions and an overview of the Migros data scraping and analysis project. The project involves scraping data from the Migros website using Python scripts, cleaning the data, storing it in a MariaDB database, and performing data analysis to answer specific questions.

## Prerequisites
Before you begin, ensure that you have the following modules and connectors installed on your machine:
- **bs4** (Beautiful Soup)
- **selenium**
- **pandas**
- **numpy** (used in a few scripts)
- **time**
- **datetime**
- **sys**
- **mariadb**

You can install these modules using pip:
```bash pip install bs4 selenium pandas numpy mariadb```


## Getting the Code

You can download all the project code from Student B (Daniele Buson) using the following GitHub repository link:
[https://github.com/DanieleBuson/Migros_Scraping_Python_HSLU_CIP](https://github.com/DanieleBuson/Migros_Scraping_Python_HSLU_CIP)

To clone the repository from the terminal in PyCharm or VSCode (ideal for the project), follow these steps:

1. Create a directory for the project.
2. Run the following commands in your terminal:

```bash git clone https://github.com/DanieleBuson/Migros_Scraping_Python_HSLU_CIP```

## Using the Code

### 1. Data Scraping

- Start with the `scraping_automated` script to extract data from the Migros website.
- Follow these steps for each script:
    1. When the page appears for the first time, click on the brand menu and wait for the page to close.
    2. After a few seconds, another page will appear. Scroll until you find the "see the next 100 products" button and click it repeatedly until you can see all the products.
    3. Wait for Beautiful Soup to process the data.
    4. Repeat this process for every script to extract all the necessary data.
    5. Several datasets will be created at this point, containing raw data that needs to be cleaned.

### 2. Data Cleaning

- Navigate to the "cleaning data" folder and run the code for each script.
- Detailed code explanations can be found inside the folder in a TXT documentation.
- After this process, you should see numerous TXT files in the data folder.

### 3. Data Storage in MariaDB

- The cleaned data files are sent to MariaDB using the MariaDB connector for Python.
- To set up MariaDB for this project:
    1. Install MariaDB, the connector for Python, and configure the username and password.
    2. You can use the following script to create a new user in MariaDB:

    ```bash
    mysql -u root -p
    ```

    3. Inside MariaDB, execute these commands:

    ```sql
    use "NAME_TABLE"; -- not mandatory
    create user "NAME_OF_THE_USER"@"localhost" identified by "PASSWORD_OF_THE_USER";
    grant all privileges on NAME_TABLE.* to "NAME_OF_THE_USER"@"localhost";
    ```

    4. Update the connection information in the Python code.
 
### 4. Data Consolidation

- The cleaned CSV files are merged into different datasets containing all the data from various food categories.
- There are primarily two types of datasets: one with quantity in grams and another with quantity in liters.
- The date is stored in separate CSV/TXT files.

### 5. Answering Questions

- Questions raised during the project are answered in the "question_solution" file.
- Note that some issues with PyCharm and CSV usage were encountered (especially in the third question solution). It is recommended to use VSCode for a smoother experience.

Please follow these steps carefully to replicate and extend the Migros data scraping and analysis project. For any questions or issues, feel free to contact the project author, Daniele Buson.

Thank you for your interest in our project!

