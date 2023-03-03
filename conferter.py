from bs4 import BeautifulSoup
import requests
response = requests.get("https://bank.gov.ua/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", class_="value-full")
    res = soup_list[1]
b = int(input())
print (b * (float(res)))
