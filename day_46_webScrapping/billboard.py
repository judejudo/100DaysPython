import requests
from bs4 import BeautifulSoup

class Billboard :
    def __init__(self,url):
        self.url = url
    
    def get_to_100_songs(self,selectors):
        response = requests.get(self.url)
        billboard_website = response.text
        soup = BeautifulSoup(billboard_website, "html.parser")
        song_name_spans = soup.select(selectors)
        song_names = [song.getText().strip() for song in song_name_spans]
        return song_names