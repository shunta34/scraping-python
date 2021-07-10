# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.python.org/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text)

# print(soup.find_all('h2'))
# print(soup.find_all('h2')[0])
# print(soup.find('h2') == soup.find_all('h2')[0])
# print(soup.find('h2').text)
# print(soup.find_all('h2').text)
# for i, h2_tag in enumerate(soup.find_all('h2')):
#   print(i, h2_tag.text)

# h2_text_list = []
# for i, h2_tag in enumerate(soup.find_all('h2')):
#   h2_text_list.append(h2_tag.text)
# print(h2_text_list)
