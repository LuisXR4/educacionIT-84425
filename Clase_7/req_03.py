import requests

r = requests.get("https://www.lanacion.com.ar/el-mundo/donald-trump-anuncia-un-alto-al-fuego-entre-el-libano-e-israel-nid16042026/")

print(r.text)