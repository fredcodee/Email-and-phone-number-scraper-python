import requests
from bs4 import BeautifulSoup
import csv
import re

url = 'http://cafeteriagroup.com'
all_links=[]

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
links = [n.get('href') for n in soup.find_all('a')]

#filter links
for i in links:
  if "contact" in i or "Contact" in i  or "Career" in i or "career" in i or 'about' in i or "About" in i or 'Services' in i or 'services' in i :
    all_links.append(i)

#get mails
name= url.split("//")
csv_file = open(name[-1], 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Emails"])

for n in all_links:
  data = requests.get(n)
  emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
  csv_writer.writerow([emails])


csv_file.close()
