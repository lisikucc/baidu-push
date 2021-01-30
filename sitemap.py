import re
import urllib
import requests

page = 'https://www.lisiku.com/sitemap.xml'
post = 'https://www.lisiku.com/sitemap.xml'

html = urllib.request.urlopen(page).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('urls-page.txt', 'w') as file:
  for data in result:
    print( data + '\n')
    file.write(data + '\n')
file.close()

html = urllib.request.urlopen(post).read().decode('utf-8')
result = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)

with open('urls-post.txt', 'w') as file:
  for data in result:
    print( data + '\n')
    file.write(data + '\n')
file.close()
