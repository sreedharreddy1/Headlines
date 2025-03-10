import requests
from bs4 import BeautifulSoup
import csv

# Fetch the web page
url = 'https://indianexpress.com/article/explained/explained-sci-tech/corpse-flower-rotting-meat-9799221/?utm_source=Taboola_Recirculation&utm_medium=RC&utm_campaign=IE&tbref=hp'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Parse HTML and extract data
headlines = []
# Replace with the specific tags and classes from Indian Express
for item in soup.find_all('h1'):
    headlines.append(item.text.strip())

for item in soup.find_all('h2'):
    headlines.append(item.text.strip())

for item in soup.find_all('h3'):
    headlines.append(item.text.strip())

# Save data to a CSV file
with open('headlines.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline'])
    for headline in headlines:
        writer.writerow([headline])

print("Headlines have been saved to 'headlines.csv'")
