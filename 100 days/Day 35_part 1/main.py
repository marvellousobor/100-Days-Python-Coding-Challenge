from bs4 import BeautifulSoup
import requests

date = input("What  would you like to travel to in YY-MM-DD format?")
top_100_list_link = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(top_100_list_link)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)