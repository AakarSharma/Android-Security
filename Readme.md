# PlayStore WebScrapper

This Code scraps the details of a particular app from the playstore website. The sites mentioned in the **input.txt** is taken as input and the output is stored in the **output.txt**.

## Requirements to run
To run this program the libraries needed with python(version 3) is
- Beautiful Soup (pip3 install bs4)
- Html2text (pip3 install html2text)
- Selenium (pip3 install selenium)
- Chrome driver to run selenium

## Running the program
```
python3 try.py
```
## Caution
To run the web scrapper on muntiple sites the time taken for one website in taken as 2 seconds. If your internet connection is slow then you need to update the **line 35** of your code to the time you prefer for it to work properly (depends on your internet connection).