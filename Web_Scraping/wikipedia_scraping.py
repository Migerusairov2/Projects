from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/139.0.0.0 Safari/537.36"
}

# or-----------
# headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(
    url="https://en.wikipedia.org/wiki/Web_scraping",
    headers=headers
)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Method 1: Using find
    heading = soup.find(id="firstHeading")
    print("Heading (method 1):", heading.text)

    # Method 2: Using CSS selector
    heading2 = soup.select_one("#firstHeading")
    print("Heading (method 2):", heading2.text)
