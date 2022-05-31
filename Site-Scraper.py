#Very simple webscraper
# to build a web scraper you can use the following libs:
# -Requests
# -Beautiful Soup
# -lxml
# -Selenium
# lets use requests
#put your website in the url

import requests
url="https://yoursite.com/"
responses = requests.get(url)
print(responses.text)