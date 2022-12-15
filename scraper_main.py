from serpapi import GoogleSearch
import os, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import csv
import cv2

image_results = []
def scraper(api_key, quer, location):
    params = {
      "q": quer,
      "hl": "en",
        "tbm": "isch",                    
        "num": "100",                     
        "ijn": 0,
      "gl": "us",
      "domain": "images.google.com",
      "api_key": api_key
    }

    search = GoogleSearch(params)         

    images_is_present = True
    while images_is_present:
        results = search.get_dict()       
        if "error" not in results:
            for image in results["images_results"]:
                if image["thumbnail"] not in image_results:
                        image_results.append(image["thumbnail"])

    # update to
            params["ijn"] += 1
        else:
            images_is_present = False
            print(results["error"])
    dirn = location+quer+"_dats"
    os.mkdir(dirn)       
    for i in range(len(image_results)):
        re1 = urllib.request.urlopen(image_results[i-1])
        arr = np.asarray(bytearray(re1.read()), dtype=np.uint8)
        ima = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        cv2.imwrite(os.path.join(dirn,quer+"_"+str(i)+".jpg"), ima)
