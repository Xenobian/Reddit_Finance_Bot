import requests
import json
from bs4 import BeautifulSoup
import os

#creating empty file
with open("company_list.txt", 'w'): pass

#function to extract 2nd and 3rd coloum from each row, and write it in the file
def scrap(url1):
    url =url1
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    html = response.content
    soup =   BeautifulSoup(html,features="html5lib")
    data = soup.find('div',attrs={'id':'content'})

    with open("company_list.txt", "a") as f:
        for row in data.findAll('tr'):
            i = 0
            for cell in row.findAll('td'):
                if i == 0:
                    i+=1
                    continue
                if i == 1:
                    f.write(cell.text.strip()+ "\n")
                if i == 2:
                    stock = cell.text.split(" ")
                    stock = " ".join(stock[:-1])
                    f.write(stock.strip()+ "\n")
                if i == 3:
                    break
                i+=1

#calling scrap() for 0-L table and L-Z table 
scrap('https://www.nseindia.com/education/content/reports/eq_research_reports_listed.htm')
scrap('https://www.nseindia.com/education/content/reports/eq_rrl_m2z.htm')