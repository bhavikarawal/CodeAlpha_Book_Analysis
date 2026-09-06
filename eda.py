import pandas as pd

# Load the dataset
df = pd.read_csv("data/books_dataset.csv")

print(df.head())
print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns)
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical summary:")
print(df.describe())
#finding avg price of books
average_price = df["Price"].mean()

print("\nAverage book price:", average_price)
#finding cheapest book
cheapest_book = df.loc[df["Price"].idxmin()]

print("\nCheapest book:")
print(cheapest_book)
#finding expensive book
most_expensive_book = df.loc[df["Price"].idxmax()]

print("\nMost expensive book:")
print(most_expensive_book)
#Find the most common rating
rating_counts = df["Rating"].value_counts()

print("\nRating distribution:")
print(rating_counts)

# avg price for each rating
average_price_by_rating = df.groupby("Rating")["Price"].mean()

print("\nAverage price by rating:")
print(average_price_by_rating)

#Check for duplicate books
print("\nDuplicate rows:")
print(df.duplicated().sum())

#duplicate book titles
print("\nDuplicate titles:")
print(df["Title"].duplicated().sum())
