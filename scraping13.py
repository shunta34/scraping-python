# import pandas as pd
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_path = '/Users/gotou/individual/public/scraping-python/chromedriver'

# options = Options()
# options.add_argument('--incognito')

# driver = webdriver.Chrome(executable_path = chrome_path, options = options)

# url = 'https://search.yahoo.co.jp/image'
# driver.get(url)

# sleep(3)

# query = 'プログラミング'
# search_box = driver.find_element_by_class_name('SearchBox__searchInput')
# search_box.send_keys(query)
# search_box.submit()

# sleep(3)

# height = 1000
# while height < 3000:
#   driver.execute_script('window.scrollTo(0, {});'.format(height))
#   height += 100
#   print(height)

#   sleep(1)

# elements = driver.find_elements_by_class_name('sw-Thumbnail')

# d_list = []

# for i, element in enumerate(elements, start = 1):
#   name = f'{query}_{i}'
#   raw_url = element.find_element_by_class_name('sw-ThumbnailGrid__details').get_attribute('href')
#   yahoo_image_url = element.find_element_by_tag_name('img').get_attribute('src')
#   title = element.find_element_by_tag_name('img').get_attribute('alt')

#   d = {
#     'filename': name,
#     'raw_url': raw_url,
#     'yahoo_image_url': yahoo_image_url,
#     'title': title
#   }

#   d_list.append(d)

#   sleep(2)

# df = pd.DataFrame(d_list)
# df.to_csv('image_urls_20210714.csv')

# driver.quit()
