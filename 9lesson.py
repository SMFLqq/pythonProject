#import requests
#res_parse_list = []
#response = requests.get("https://coinmarketcap.com/")
#response_text = response.text
#response_parse = response_text.split("<span>")
#for parse_elem_1 in response_parse:
    #if parse_elem_1.startswith("$"):
        #for parse_elem_2 in parse_elem_1.split("</span>"):
            #if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit:
                #res_parse_list.append(parse_elem_2)

#bitcoin_exchange_rate = res_parse_list[0]
#print(bitcoin_exchange_rate)




#import urllib.request
#import requests
#response = opener.open ("https://httpbin.org/")
#print(response.read())
#response = requests.get("https://httpbin.org/get")
#print(response.content)


from bs4 import BeautifulSoup
import requests
response =requests.get("https://bank.cov.ua/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div",class_="value-full")
    res = soup_list[1].find("snall")
    res2 = str(res.text)
    res3 = res2.rstep()

a = int(input())
print(int(res3) * a)