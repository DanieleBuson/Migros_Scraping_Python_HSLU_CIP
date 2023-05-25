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

4. We answered to the questions in the documentation in a file question_solution.
    4.1 We notice errors in using pycharm and csv together. Probably was due to the lack of one or more dependencies. 
        However, since the timing was quite strict, we advise the user that this particular script is surely working on VSCode.

