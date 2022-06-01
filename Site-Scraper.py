#Very simple webscraper
# to build a web scraper you can use the following libs:
# -Requests
# -Beautiful Soup
# -lxml
# -Selenium
# lets use requests
# if you do not have the pyfiglet module installed remove it from the code
# if you need pyfiglet installed copy this command in cmd line: #pip install pyfiglet
import pyfiglet
import requests
# if you do not use pyfiglet module  so remove the next 2 lines, it is for showing the banner.
ascii_banner = pyfiglet.figlet_format("WEBSCRAPER BY El3ct0r")
print(ascii_banner)
# input the website
# make sure that you input in this format https://yoursite.com/
url= input("input the website: ")

responses = requests.get(url)
print(responses.text)
