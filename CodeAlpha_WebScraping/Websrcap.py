import requests
from bs4 import BeautifulSoup
import pandas as pd

# Custom dataset storage
data = []

# Scraping multiple pages (web navigation)
for page in range(1, 6):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # Extract Title
        title = book.h3.a["title"]

        # Extract Price
        price = book.find("p", class_="price_color").text
        price = float(price.replace("$", ""))

        # Extract Rating
        rating = book.p["class"][1]

        # Extract Availability
        availability = book.find("p", class_="instock availability").text.strip()

        # Append to dataset
        data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV (Custom Dataset)
df.to_csv("custom_dataset_books.csv", index=False)

# Display dataset
print("Custom Dataset Created Successfully!")
print(df.head())