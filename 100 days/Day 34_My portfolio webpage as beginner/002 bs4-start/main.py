from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")

print(response.text)




# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title.name)
# # print(soup.prettify)
# # print(soup)
#
# # all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
# #
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))
#
# my_url = soup.select_one(selector="p a")
# print(my_url)