from bs4 import BeautifulSoup
import requests
import time

# # to get the web content

# url="https://www.w3schools.com/css/default.asp"
# req=requests.get(url)
# print("response",req.text)
# soup = BeautifulSoup(req.text, "html.parser")
# print(soup.text)

# #To get all links present in web page

# for link in soup.find_all('a'):
#     print(link.get('href'))

# To get the content of our html page
with open('E:/Jose/web_scrap.html') as fb:
    soup=BeautifulSoup(fb,'lxml')

# To run the program forever
# while True:
#     soup=BeautifulSoup('<p>newtext</p>')
#     print(soup.string)
#     time.sleep(300)


soup = BeautifulSoup('<p name="1"><!-- Everything inside it is COMMENTS --></p>','lxml')
comment = soup.p.string
type(comment)
# <class 'bs4.element.Comment'>
# <class 'bs4.element.Comment'>
print(soup.p.prettify())
print(soup)
