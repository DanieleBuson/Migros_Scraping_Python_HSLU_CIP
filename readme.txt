Please, install the following modules/connectors, if they are not already on your machine: 
    - bs4, selenium, pandas, numpy(used in just a few scripts), time, datetime, sys, mariadb

You can download all the code from Student B (me) from:
    https://github.com/DanieleBuson/Migros_Scraping_Python_HSLU_CIP
    From the terminal in Pycharm or VSCode(ideal):
    > (create a directory for the project)
    > git clone https://github.com/DanieleBuson/Migros_Scraping_Python_HSLU_CIP

How to use this code:

1. starting from scraping_automated, the user should be able to extract all the data.
    1.1 In each script, when the page appears for the first time, click on the brand menu and wait for the page to close
    1.2 After a few seconds, another page will appear. Scroll until the button "see the next 100 products" and click it until you 
        can see all the products. 
    1.3 Once it is done wait for BeutifulSoup to do its job. 
    1.4 Repeat the process for every script. You should be able to extract all the data, there is enough time thanks to time.sleep().
        If it is not enough change the number in time.sleep(). 
    1.5 Lot of datasets are created at this point. These contain raw data that has to be cleaned 

2. After scraping the data go to the folder cleaning data and run the code of each script. 
    2.1 More details regarding the code can be found inside the folder in a txt documentation. 
    2.2 After this process you should be able to see lot of txt files in the data folder.

3. The file were sent to Mariadb using the mariadb connector for Pyhton.
    3.1 it is important to install mariadb, the connector for Python and to change the password and user in the 
        configuration. In my case, the user is created from the user root, it is called daniele and it is identified by the password 
        mypass.
    3.2 You can use the following script to create your own users in mariadb:
        > mysql -u root -p
        > > insert password of root
        > (inside mariadb) use "NAME_TABLE"; -not mandatory- 
        > (inside mariadb) create user "NAME_OF_THE_USER"@"localhost" identified by "PASSWORD_OF_THE_USER";
        > (inside mariadb) grant all privileges on NAME_TABLE.* to "NAME_OF_THE_USER"@"localhost";
    3.3 Once it is done change the connection also in the python code. 

4. The csv file cleaned were merged into a different daatsets that contain all the data from all the category of food. 
    There are mainly two types, the first one presents the quantity in grams, the second one presents the quantity in liters.
    We store the date in anotehr csv/txt files. 

5. We answered to the questions in the documentation in a file question_solution.
    4.1 We notice errors in using pycharm and csv together (especially in the third question solution). Probably was due to 
    the lack of one or more dependencies. However, since the timing was quite strict, we advise the user 
    that this particular script is surely working on VSCode.




