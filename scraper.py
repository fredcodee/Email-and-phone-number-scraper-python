import requests
import re
from csv import writer

# get the data
data = requests.get('type url link here')

#save extracted data to csv file
with open("scrape_list.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    headers = ["Phone","Emails"]
    csv_writer.writerow(headers)

    # extract the phone numbers, emails, whatever
    phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
    emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

    csv_writer.writerow([phones,emails])
