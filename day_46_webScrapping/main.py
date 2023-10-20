from billboard import Billboard
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from  dotenv import load_dotenv



date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD ")
url =f"https://www.billboard.com/charts/hot-100/{date}" 
selectors = "li ul li h3"

billboard = Billboard(url)
billboard.get_to_100_songs(selectors)

load_dotenv()
auth_manager = SpotifyClientCredentials()
