from bs4 import BeautifulSoup
import requests
# import lxml

# with open("website.html",encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# heading = soup.find(name="h1", id="name")

# section = soup.find(name="h3", class_="heading")
# company_url = soup.select_one(selector="p em strong a")
# headings =soup.select(".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
name = soup.find(name="a", class_="storylink")
print(name)
