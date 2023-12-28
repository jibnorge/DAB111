# WebScraper-FlaskDB
## Project description

The Python script performs web scraping on the "Books to Scrape" website (https://books.toscrape.com/) to extract information about various books, including their names, prices and other features. The data is then stored in SQLite database and later presented through a Flask web application. The coding is done in both .py and .ipynb formats.


## Data Collection

The data for this project was collected from 'http://books.toscrape.com/' website through web scraping using the BeautifulSoup library.

## Data Processing 

The collected data was processed with some basic cleaning actions such as text normalisation , case adjustment and numerical value extraction.

## Database

The data was stored in SQlite database which is named as "books.db" which has two tables one containing the data and other contaning the feature details.


## Website 

The Flask framework, along with the sqlalchemy package, was used to create a simple website containing the tabular representation of scraped data. A simple template was choosen from w3schools for creating the outline of this website. There is also an About page describing data along with variable definitions.

## Project Structure

```plaintext
- WebScraper-FlaskDB
    - templates/
    - README.md
    - book_data.csv
    - books_updated.csv
    - books.db
    - data_collection.ipynb
    - data_collection.py
    - data_preprocessing.ipynb
    - data_preprocessing.py
    - database.ipynb
    - database.py
    - features.csv
    - README.md
    - requirements.txt
    - website.ipynb
    - website.py
```

## Code Usage 

1. Setting up the environment
- Clone the repository 
```bash
git clone https://github.com/jibnorge/WebScraper-FlaskDB.git
cd WebScraper-FlaskDB
```

- Create a virtual python environment in anaconda prompt
```bash
conda create --name venv python=3.9
```

- Activate the environment and install requirements.txt
```bash
conda activate venv
pip install -r requirements.txt
```

- Run the web app or open jupyter notebook and run the **website.ipynb** file.
```bash
python website.py
```


## Conclusion
This project demonstrates the end-to-end process of web scraping, data processing, database management, and website development. The project's aim is to provide a comprehensive understanding of these concepts through a practical implementation. 
