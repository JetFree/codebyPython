import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = "https://vdoh.ru/whatever/list/znamenitosti"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find('div', id="pt").find_all("a")
    for link in links:
        print(link.text)

