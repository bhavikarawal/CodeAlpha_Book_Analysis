# Book Data Analysis Using Python

## Project Overview

This project demonstrates a complete data analytics workflow using web scraping, exploratory data analysis, and data visualization.

The project collects book information from the public website Books to Scrape and analyzes the collected dataset using Python.

## Objectives

* Extract book information from a public website.
* Create a structured dataset from the scraped information.
* Perform exploratory data analysis to understand the dataset.
* Identify patterns and trends in book prices and ratings.
* Create visualizations to communicate the findings.

## Tools and Technologies

* Python
* Requests
* BeautifulSoup
* Pandas
* Matplotlib
* Visual Studio Code

## Project Workflow

### 1. Web Scraping

The `web_scraping.py` script uses the Requests library to retrieve webpage content and BeautifulSoup to parse the HTML.

The scraper navigates through 10 pages and collects information about 200 books, including:

* Book title
* Price
* Rating
* Availability
* Product URL

The collected data is cleaned and saved as:

`data/books_dataset.csv`

### 2. Exploratory Data Analysis

The `eda.py` script uses Pandas to explore and analyze the dataset.

The analysis includes:

* Dataset shape
* Column names
* Data types
* Missing-value analysis
* Duplicate-value analysis
* Statistical summary
* Average book price
* Cheapest and most expensive books
* Rating distribution
* Average price by rating

## Key Findings

* The dataset contains **200 books** and **5 columns**.
* The average book price is approximately **£34.80**.
* The cheapest book in the dataset is **Patience**.
* The most expensive book is **Thomas Jefferson and the Tripoli Pirates**.
* One-star books are the most common rating category, with **49 books**.
* Three-star books are the least common rating category, with **35 books**.
* Three-star books have the highest average price at approximately **£36.19**.
* Two-star books have the lowest average price at approximately **£33.74**.
* The difference in average prices across rating categories is relatively small, suggesting no strong relationship between rating and price in this dataset.
* There are **no duplicate rows** and **no duplicate book titles**.

## 3. Data Visualization

The `visualization.py` script uses Matplotlib to create four visualizations:

1. **Distribution of Book Ratings**
2. **Distribution of Book Prices**
3. **Average Book Price by Rating**
4. **Top 10 Most Expensive Books**

The visualization files are available in the `visualizations` folder.

## Conclusion

This project demonstrates the process of collecting data from a public webpage, organizing and cleaning the collected information, performing exploratory analysis, and presenting the findings through visualizations.

The project provides practical experience with Python libraries commonly used in data analytics and demonstrates how raw web data can be transformed into a structured dataset and meaningful insights.






