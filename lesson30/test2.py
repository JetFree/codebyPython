import requests
from bs4 import BeautifulSoup


def parse_names(html):
    soup = BeautifulSoup(html, "html.parser")
    h3_list = soup.find_all("h3", attrs={"class", "contentRow-header"})
    name_list = list()
    for tag in h3_list:
        name_list.append(tag.find("span").text)
    return name_list


if __name__ == '__main__':
    url = "https://codeby.net/members/?key=staff_members"
    html = requests.get(url).text
    for name in parse_names(html):
        print(name)
