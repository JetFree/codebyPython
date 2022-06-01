import requests
from bs4 import BeautifulSoup


def get_page_data(html):
    res = BeautifulSoup(html.text, 'lxml')
    line = res.find("loc")
    if line:
        for i in line:
            print(i.text)
    else:
        print("There is no loc element found in html!")


def get_sitemap():
    print("8. sitemap.xml\n")
    url = input("Enter host [https://site.com]: ")
    if url:
        if url[-1] == '/':
            page = requests.get(url + "sitemap.xml")
        else:
            page = requests.get(url + "/sitemap.xml")
        if page.status_code == 200:
            get_page_data(page)
        else:
            print('File "sitemap.xml" not found!')