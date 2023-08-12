from bs4 import BeautifulSoup

with open(file="day_46_webScrapping/website.html", encoding="utf8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")

soup.find_all(name="a")
