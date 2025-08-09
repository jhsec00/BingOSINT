import openpyxl 
import requests
import time
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)      


filename = "BingSearchResult_0724_1600.xlsx" 
book = openpyxl.load_workbook(filename)

sheet=book.worksheets[0]
data = []
for row in sheet.rows:
    data.append([
        row[2].value
    ])


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
for i in range(159, len(data)):
    res = requests.get(url=data[i][0], headers=headers, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    for link in soup.find_all('title'):
        print(f"{i}/{len(data)} {link.text} {data[i][0]} ")
    time.sleep(2)