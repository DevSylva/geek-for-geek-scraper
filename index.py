import  requests
from bs4 import BeautifulSoup

# Making a Get Request
r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

print(r)

soup = BeautifulSoup(r.content, "html.parser")

s = soup.find('div', class_='entry-content')
 
lines = s.find_all('p')
 
for line in lines:
    print(line.text)



# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))


images_list = []
 
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)