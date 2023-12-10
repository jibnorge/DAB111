# Python Web Scraping Project 

## Project description

This Python script performs web scraping on the "Books to Scrape" website (https://books.toscrape.com/) to extract information about various books, including their names and prices. The python script utilizes the BeautifulSoup library for parsing HTML and the requests library for fetching the web page.


## Data Collection

The data for this project was collected from 'http://books.toscrape.com/' website through web scraping.

## Data Processing 

The collected data was processed with some basic cleaning actions such as text normalisation , case adjustment and numerical value extraction.

## Database

The data was stored in SQlite database which is named as "books.db" which has two tables one containing the data and other contaning the feature details.


## Website 

Flask is a lightweight Python web framework that provides useful tools and features for creating web applications in the Python Language. SQLAlchemy is an SQL toolkit that provides efficient and high-performing database access for relational databases. The Flask framework, along with the sqlalchemy package, was used to create a simple website. Our site has an About page describing data along with variable definitions.

## Project Structure

```plaintext
- DAB111
    - templates
        - about.html
        - fantasy.html
        - fiction.html
        - food_and_drink.html
        - index.html
        - mystery.html
        - non_fiction.html
        - romance.html
        - seq_art.html
        - young_adult.html
    - book_data.csv
    - books_updated.csv
    - books.db
    - data_collection.py
    - data_preprocessing.py
    - database.py
    - features.csv
    - README.md
    - requirements.txt
    - website.py
```

## Code Usage 

1. Setting up the environment
```bash
# Clone the repository
git clone https://github.com/jibnorge/DAB111.git
cd DAB111

# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```




## Conclusion
This project demonstrates the end-to-end process of web scraping, data processing, database management, and website development. Our project's aim is  to provide a comprehensive understanding of these concepts through a practical implementation. 