import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'

response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('h3')

    headline_list = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for idx, line in enumerate(headline_list, 1):
            file.write(f"{idx}. {line}\n")

    print(" Headlines scraped and saved to 'headlines.txt'")
else:
    print(" Failed to retrieve the website. Status code:", response.status_code)