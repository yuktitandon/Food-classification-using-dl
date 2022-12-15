from serpapi import GoogleSearch
import os, json

image_results = []
params = {
  "q": "Naan",
  "hl": "en",
    "tbm": "isch",                    
    "num": "100",                     
    "ijn": 0,
  "gl": "us",
  "domain": "images.google.com",
  "api_key": "enter-api-key"
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

#print(json.dumps(image_results, indent=2))
for i in range(1,25):
    try:
        re1 = urllib.request.urlopen(image_results[i-1])
        arr = np.asarray(bytearray(re1.read()), dtype=np.uint8)
        ima = cv2.imdecode(arr, cv2.IMREAD_COLOR)
        plt.subplot(10, 10, i, )
        plt.title(i)
        plt.axis("off")
        plt.imshow(ima)
    except urllib.request.HTTPError:
        pass
