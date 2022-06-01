import requests


def get_page_data(html):
    res = html.text
    print(res)


def show_robots_content():
    print("7. robots.txt\n")
    url = input("Enter host [https://site.com]: ")
    head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64} AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    if url[-1] == "/":
        page = requests.get(url + 'robots.txt', headers=head)
    else:
        page = requests.get(url + "/robots.txt", headers=head)
    if page.status_code != 404:
        get_page_data(page)
    else:
        print("File 'robots.txt' not found!")