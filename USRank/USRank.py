# author : Charles
# time   ：2019/9/4  11:45 
# file   ：USRank.PY
# PRODUCT_NAME  ：PyCharm

import requests
from lxml import etree
import pandas as pd
url="http://www.qianmu.org/2019USNEWS%E7%BE%8E%E5%9B%BD%E7%BB%BC%E5%90%88%E6%80%A7%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D"
headers={
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
         }
resp=requests.get(url,headers=headers)
# enconding = requests.utils.get_encodings_from_content(resp.text)
# print(enconding)

html_doc = resp.content.decode("utf-8")

with open('test.html', 'w') as f:
    f.write(html_doc)

tree = etree.HTML(html_doc)
path1="/html/body/div[2]/div[5]/div/div/div/div/div/div[2]/div/div[1]/div[2]/table/tbody/tr//text()"
node = tree.xpath(path1)
newlist=[]
for i in node:
    if i !='\t' and i != '\t\t' and i != '\t\t\t':
        newlist.append(i)
result = [newlist[i:i+8] for i in range(0,len(newlist),8)]
# print(result)
df = pd.DataFrame(result)
df.to_excel("USRank.xlsx", index=False)