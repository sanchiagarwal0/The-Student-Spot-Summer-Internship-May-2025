import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape (a demo book website)
url = "http://books.toscrape.com/"

try:
    # Send HTTP request
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status codes
    
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all book containers
    books = soup.find_all('article', class_='product_pod')
    
    # Prepare to store scraped data
    scraped_data = []
    
    # Extract information from each book
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        scraped_data.append({'title': title, 'price': price})
    
    # Save to CSV file
    with open('books_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(scraped_data)
    
    print(f"Successfully scraped {len(scraped_data)} books. Data saved to books_data.csv")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
except Exception as e:
    print(f"An error occurred: {e}")