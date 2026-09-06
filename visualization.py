import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/books_dataset.csv")

# -------------------------------
# CHART 1: Rating Distribution
# -------------------------------

rating_counts = df["Rating"].value_counts()

plt.bar(rating_counts.index, rating_counts.values)

plt.xlabel("Book Rating")
plt.ylabel("Number of Books")
plt.title("Distribution of Book Ratings")

plt.savefig("visualizations/rating_distribution.png")
plt.show()
plt.close()


# -------------------------------
# CHART 2: Price Distribution
# -------------------------------

plt.hist(df["Price"], bins=10)

plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Distribution of Book Prices")

plt.savefig("visualizations/price_distribution.png")
plt.show()
plt.close()


# --------------------------------------
# CHART 3: Average Price by Rating
# --------------------------------------

average_price_by_rating = df.groupby("Rating")["Price"].mean()

plt.bar(
    average_price_by_rating.index,
    average_price_by_rating.values
)

plt.xlabel("Book Rating")
plt.ylabel("Average Price (£)")
plt.title("Average Book Price by Rating")

plt.savefig("visualizations/average_price_by_rating.png")
plt.show()
plt.close()

# --------------------------------------
# CHART 4: Top 10 Most Expensive Books
# --------------------------------------

top_10_expensive = df.nlargest(10, "Price")

plt.barh(
    top_10_expensive["Title"],
    top_10_expensive["Price"]
)

plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.title("Top 10 Most Expensive Books")

plt.savefig("visualizations/top_10_expensive_books.png")
plt.show()
plt.close()