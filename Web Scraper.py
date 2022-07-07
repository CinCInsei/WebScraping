import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='E:/CIS403 python.2/project4/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs='lazyload-wrapper '):
    name = element.find('h5')
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')
