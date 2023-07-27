import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.carrefoursa.com/sade-maden-sulari/c/1413?q=%3AbestSeller%3AinStockFlag%3Atrue&text=#')

# carrefour SA
select_soda_product_carrefour = driver.find_elements(By.XPATH,
                                                     "/html/body/main/div[@class='container']//div[@class='pl-grid-cont']/ul/li")
carrefour_soda = []
update_carrefour_soda = []
for value in select_soda_product_carrefour:
    carrefour_soda.append(value.text)

for value in carrefour_soda:
    soda = value.split('\n')
    update_carrefour_soda.append(soda)
carrefour_soda.clear()
for value in update_carrefour_soda:
    x = value[0:2]
    carrefour_soda.append(x)

update_carrefour_soda.clear()

carrefour_soda_title = []
carrefour_soda_price = []
for i in range(15):
    carrefour_soda_title.append(carrefour_soda[i][0])
    carrefour_soda_price.append(carrefour_soda[i][1])

df_carrefour = pd.DataFrame({"Market": "carrefour SA","title": carrefour_soda_title, 'price': carrefour_soda_price})


# Migros
driver.get('https://www.migros.com.tr/arama?q=soda&sayfa=1&kategori=133&27=123&sirala=akilli-siralama')
time.sleep(5)
select_soda_migros_title = driver.find_elements(By.CLASS_NAME, "product-name")
driver.implicitly_wait(2)

migros_soda_title = []
for i in select_soda_migros_title:
    migros_soda_title.append(i.text)

migros_soda_price = []
select_soda_migros_price = driver.find_elements(By.CLASS_NAME, "amount")
for i in select_soda_migros_price:
    migros_soda_price.append(i.text)
migros_soda_price.pop(0)

df_migros = pd.DataFrame({"Market": "migros",'title': migros_soda_title, 'price': migros_soda_price})



# A101
driver.get('https://www.a101.com.tr/list/?search_text=soda&personaclick_search_query=soda&personaclick_input_query=soda')
time.sleep(5)
select_soda_a101_title = driver.find_element(By.XPATH, "/html/body[@class='page-inner']/section[@class='js-main-wrapper']/section[3]/div[3]//ul[@class='product-list-general']//article/a[@title='Beypazarı Maden Suyu 200 ml']//h3[@class='name']")
soda_a101_title = [select_soda_a101_title.text]

select_soda_a101_price = driver.find_element(By.XPATH, "/html/body[@class='page-inner']/section[@class='js-main-wrapper']/section[3]//ul[@class='product-list-general']//article/a[@title='Beypazarı Maden Suyu 200 ml']//section[@class='prices']/span[@class='current']")
soda_a101_price = [select_soda_a101_price.text]

df_a101 = pd.DataFrame({'Market': "A101", 'title': soda_a101_title, 'price': soda_a101_price})


# ŞOK MARKET
driver.get("https://www.sokmarket.com.tr/arama/maden%20suyu")
time.sleep(5)

soda_sok_title = []
select_soda_sok_title_1 = driver.find_element(By.XPATH, "/html//div[@id='root']/section//ul[@class='results-list']//a[@href='/eskipazar-maden-suyu-200-ml-p-2204']//strong[@class='content-title']")
soda_sok_title.append(select_soda_sok_title_1.text)

select_soda_sok_title_2 = driver.find_element(By.XPATH, "/html//div[@id='root']/section//ul[@class='results-list']//a[@href='/eskipazar-maden-suyu-6200ml-p-2205']//strong[@class='content-title']")
soda_sok_title.append(select_soda_sok_title_2.text)

select_soda_sok_title_3 = driver.find_element(By.XPATH, "/html//div[@id='root']/section//ul[@class='results-list']//a[@href='/kizilay-sade-maden-suyu-6200-ml-p-2203']//strong[@class='content-title']")
soda_sok_title.append(select_soda_sok_title_3.text)

soda_sok_price = []
select_soda_sok_price_1 = driver.find_element(By.XPATH, "/html//div[@id='root']/section/main[@class='listing-results']//ul[@class='results-list']//a[@href='/eskipazar-maden-suyu-200-ml-p-2204']//span[.='3,90']")
soda_sok_price.append(select_soda_sok_price_1.text)

select_soda_sok_price_2 = driver.find_element(By.XPATH, "/html//div[@id='root']/section/main[@class='listing-results']//ul[@class='results-list']//a[@href='/eskipazar-maden-suyu-6200ml-p-2205']//span[.='18,75']")
soda_sok_price.append(select_soda_sok_price_2.text)

select_soda_sok_price_3 = driver.find_element(By.XPATH, "/html//div[@id='root']/section/main[@class='listing-results']//ul[@class='results-list']//a[@href='/kizilay-sade-maden-suyu-6200-ml-p-2203']//span[.='18,75']")
soda_sok_price.append(select_soda_sok_price_3.text)

df_sok = pd.DataFrame({'Market': "SOK Market", 'title': soda_sok_title, 'price': soda_sok_price})


frames = [df_carrefour,df_migros, df_a101, df_sok]
result = pd.concat(frames)
result.to_csv('markets_soda_price.csv')