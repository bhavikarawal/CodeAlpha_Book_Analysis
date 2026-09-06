import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Store all scraped data
data = []

# Scrape first 10 pages
for page in range(1, 11):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping page {page}...")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Could not access page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books on the page
    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        relative_url = book.h3.a["href"]

        product_url = "https://books.toscrape.com/catalogue/" + relative_url

        price = book.find(
            "p", class_="price_color"
        ).text.strip()

        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        })

    # Small delay between requests
    time.sleep(1)


# Convert scraped data into DataFrame
df = pd.DataFrame(data)

df["Price"] = (
    df["Price"]
    .str.replace("Â", "", regex=False)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"])
# Save dataset
df.to_csv("data/books_dataset.csv", index=False)

print("\nScraping completed!")
print("Total books collected:", len(df))
print("\nFirst 5 records:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nMissing values:")
print(df.isnull().sum())