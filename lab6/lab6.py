import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

url=input('Enter the URL:\n')

def parse(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'html.parser') 
    return soup

page=parse(url)
content=page.find('div', 'content-article')

def inside():
    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'html.parser')
    i=0
    for link in soup.find_all('a', href=True):
        i+=1  
        text=page.find('div', 'content-article')
        img=len([tag.name for tag in page.find_all('img')])
        links=len([tag.name for tag in page.find_all('link')])
        tags=len([tag.name for tag in page.find_all()])

    print('В тексте:')
    print('Изображений:', img)
    print('Тегов:', tags)
    print('Ссылок:', links)
print(inside())