import urllib.request
from bs4 import BeautifulSoup as b4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import csv
import cv2
import os
def get_img(quer):
    im = "https://www.google.com/search?q="+quer+"&hl=en&authuser=0&tbm=isch&sxsrf=ALiCzsY92VOIq1NKz-LpP8aLGDn9tKAaZg%3A1670916527836&source=hp&biw=1440&bih=684&ei=rymYY_jNMO2F4t4PvuyF6As&iflsig=AJiK0e8AAAAAY5g3v-udnPDV400p02Oufkcyd4kyn1p2&oq=&gs_lcp=CgNpbWcQARgAMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnMgcIIxDqAhAnUABYAGDFEGgBcAB4AIABAIgBAJIBAJgBAKoBC2d3cy13aXotaW1nsAEK&sclient=img"
    pa=requests.get(im)
    print(pa.status_code)
    paa = b4(pa.content, 'html.parser')
    da = paa.find_all('img',{'class':"yWs4tf"})
    links = []
    for i in da:
        links.append(i['src'])
    count = 1
    dirn = "user-directory-input-here"+quer+"_dats"
    os.mkdir(dirn)
    for i in range(len(links)):
        re = urllib.request.urlopen(links[i])
        arr = np.asarray(bytearray(re.read()), dtype=np.uint8)
        ima = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        cv2.imwrite(os.path.join(dirn,quer+"_"+str(count)+".jpg"), ima)
        cv2.imwrite(quer+"/"+quer+"_"+str(count)+".jpg", ima)
        count+=1
'''
df = pd.read_excel("/Users/jangayarkanni/Desktop/GAIP/food.xlsx")
dfv = df[df['Vegetarian/Non-Vegetarian']=="Non-Vegetarian"]
lis = list(dfv['Name'])
val = list()
for j in range(len(lis)):
    print(lis[j])
    val.append('_'.join(lis[j].split()))
for i in range(len(lis)):
    get_img(val[i])

'''
