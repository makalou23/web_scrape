import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/mohamedmakalou/Downloads/chromedriver')
driver.get('https://oxylabs.io/blog')
result = []
new = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for element in soup.findAll("h5", attrs={'class': 'css-1rz2iog e1nywbhn4'}):
    if element not in result:
        result.append(element.text)
df = pd.DataFrame({'Names': result})
df.to_csv('names.csv', index=False, encoding='utf-8')
print(result)
