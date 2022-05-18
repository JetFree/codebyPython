import requests
from bs4 import BeautifulSoup


def parse_all_proxies(pages):
    proxy_list = list()
    for page in pages:
        html = requests.get(page).text
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.find("tbody").find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            proxy_list.append(f"{cells[1].text}:{cells[2].text}")
    return proxy_list


def find_all_pages():
    pages = list()
    html = requests.get(domain + url).text
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find("div", class_="pager").find_all("a")
    pages.append(domain + url)
    for link in links:
        pages.append(domain + link.get("href"))
    return pages


if __name__ == '__main__':
    domain = "http://foxtools.ru"
    url = "/Proxy"
    pages = find_all_pages()
    for proxy in parse_all_proxies(pages):
        print(proxy)
