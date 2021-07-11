# import requests
# from bs4 import BeautifulSoup

# url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}'
# target_url = url.format(1)
# print(target_url)
# r = requests.get(target_url)
# soup = BeautifulSoup(r.text)

# contents = soup.find_all('div', class_ = 'cassetteitem')
# print(len(contents))
# content = contents[0]

# detail = content.find('div', class_ = 'cassetteitem-detail')
# table = content.find('table', class_ = 'cassetteitem_other')

# title = detail.find('div', class_ = 'cassetteitem_content-title').text
# address = detail.find('li', class_ = 'cassetteitem_detail-col1').text
# access = detail.find('li', class_ = 'cassetteitem_detail-col2').text
# age = detail.find('li', class_ = 'cassetteitem_detail-col3').text
# print(title, address, access, age)

# tr_tags = table.find_all('tr', class_ = 'js-cassette_link')
# tr_tag = tr_tags[0]
# print(tr_tag.find_all('td'))
# print(tr_tag.find_all('td')[2:6])
# floor, price, first_fee, capacity = tr_tag.find_all('td')[2:6]
# print(floor, price, first_fee, capacity, )
