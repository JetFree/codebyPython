from ftplib import FTP
import requests


def upload_file_ftp(username, password, file_name):
    ftp = FTP("localhost")
    ftp.login(username, password)
    with open(file_name, "r+b") as fp:
        ftp.storbinary(f"STOR {file_name}", fp)
    ftp.quit()


if __name__ == "__main__":
    image_url = "https://i.ytimg.com/vi/VKErEwtJ-Nw/maxresdefault.jpg"
    file = "winner.jpg"
    res = requests.get(image_url, stream=True)
    res.raise_for_status()
    with open(file, "w+b") as f:
        for i in res.iter_content(chunk_size=64000):
            f.write(i)
    upload_file_ftp("ftpuser", "kali", file)
    print("Файл скачан и загружен на FTP-сервер")
