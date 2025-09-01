from bs4 import BeautifulSoup
import os
import pandas as pd
import re



product =[]

for file in os.listdir("data"):
    with open(f"data/{file}","r",encoding="utf-8") as f:
        html_doc = f.read()
    soup =BeautifulSoup(html_doc, 'html.parser')
    p= soup.find("h2")
    t =soup.find("span",attrs={"class":'a-price-whole'})
    b =soup.find("h2",attrs={"class":'a-size-base-plus a-spacing-none a-color-base a-text-normal'})
    title = p.get_text()
    price = t.get_text()
    brand = b.get_text()       
    availability = "In Stock"
    price = re.sub(r"[^\d]", "", price)
    if int(price) <2000:    
        product.append({
        "Watch Name": title,
        "Brand": brand,
        "Price": price,
        "Availability": availability,
        })
        
df = pd.DataFrame(product)
df.to_excel("amazon_watches.xlsx", index=False)

print("Data saved to amazon_watches.xlsx")
