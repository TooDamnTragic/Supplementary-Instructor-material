import requests
from bs4 import BeautifulSoup
import os

# Fetch the page content
url = "https://highfalutin-past-stoat.glitch.me"
response = requests.get(url)

# Parse the content
soup = BeautifulSoup(response.text, "html.parser")

# Save HTML
with open("frankenstein_lab.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# Download additional assets (CSS, JS, images)
for link in soup.find_all(["script", "link", "img"]):
    asset_url = link.get("src") or link.get("href")
    if asset_url:
        asset_url = os.path.join(url, asset_url.lstrip('/'))
        asset_content = requests.get(asset_url).content
        asset_name = os.path.basename(asset_url)
        with open(asset_name, "wb") as f:
            f.write(asset_content)
