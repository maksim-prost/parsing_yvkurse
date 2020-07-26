import requests
from bs4 import BeautifulSoup as BS
from config import token
from vk_api_my import VkApi

code = """
    return API.wall.get(
    {'offset':%s,'count':100,'domain':'yvkurse'}).items@.attachments;
"""
vk = VkApi(token=token)
offset=0
list_url=[]
r = True
while r:
    r = vk.method('execute',{'code':code%offset})
    for public in r: 
        if public and 'link' in public[0] and public[0]['link']["description"] and public[0]['link']["description"]== "Статья":
            list_url.append(public[0]['link']['url'])
    offset += 100

print(list_url, len(list_url),sep='\n')