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

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text


soup = BeautifulSoup(yc_web_page, "html.parser")
movie_list = []
sum = 100
for item in soup.findAll(name="h3", class_="title"):
    movie_name= item.get_text()
    # print (movie_name)
    if movie_name == "12: The Godfather Part II":
        movie_list.append(f"{sum}: {movie_name.split(':', 1)[1].strip()}")
    else:
        movie_list.append(f"{sum}) {movie_name.split(')', 1)[1].strip()}")
    sum = sum - 1

# print(len(movie_list))
reversed_movie_list = movie_list[::-1]

with open("day_45_webscrapping/movies_file.txt", "w", encoding='utf-8') as file:
    for movie in reversed_movie_list:
        file.write(f"{movie}\n")