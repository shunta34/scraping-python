# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.python.org/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text)

# print(len(soup.find_all('span')))
# print(soup.find_all('span'))
# print(soup.find_all('span', class_ = 'say-no-more'))
# print(soup.find_all('span', {'class': 'say-no-more'}))
# print(soup.find_all('span', class_ =['say-no-more', 'message']))

# url = 'https://tech-diary.net/python-scraping-books/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text)

# header_2_and_3 = [tag.text for tag in soup.find_all(['h2', 'h3'])]
# print(header_2_and_3)

# print(soup.find('article').find_all(['h2', 'h3']))
# body = soup.find('article')
# print(body.find_all(['h2', 'h3']))

# print(len(soup.find_all(['h2', 'h3'])))
# soup.find('h2', class_ = 'post-list-title').extract()
# print(len(soup.find_all(['h2', 'h3'])))
# print(soup.find_all(['h2', 'h3']))
