import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Women_and_video_games"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "sortable"},{"id": "Genre_preferences"})
with open("webscrapping.csv", "w") as f:
    for row in table.find_all("tr"):
        for cell in row.find_all("td"):
            f.write(cell.text + ",")
        f.write("\n")
