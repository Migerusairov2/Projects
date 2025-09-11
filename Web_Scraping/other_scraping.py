import requests
from bs4 import BeautifulSoup


def github_scraping():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    }

    response = requests.get("https://github.com/", headers=headers)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.title.text)


github_scraping()
