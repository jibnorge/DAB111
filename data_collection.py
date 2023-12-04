import requests
import bs4
import lxml
import pandas as pd
from tqdm import tqdm

title = []
category = []
upc = []
product_type = []
price_excl = []
price_incl = []
tax = []
availability = []
reviews = []

for i in tqdm(range(1,51)):
    page_url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    
    # Sending request to the page
    req = requests.get(page_url)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    
    # Extract data from each book on the page
    for book in soup.select('h3'):
        url = "https://books.toscrape.com/catalogue/"
        main_url = url + book.select('a')[0]['href']
        result = requests.get(main_url)
        
        page = bs4.BeautifulSoup(result.text, "lxml")
        
        # Extract book details
        title.append(page.select('title')[0].getText())
        category.append(page.select('.breadcrumb')[0].select('a')[2].getText())
        upc.append(page.select('.product_page')[0].select('td')[0].getText())
        product_type.append(page.select('.product_page')[0].select('td')[1].getText())
        price_excl.append(page.select('.product_page')[0].select('td')[2].getText())
        price_incl.append(page.select('.product_page')[0].select('td')[3].getText())
        tax.append(page.select('.product_page')[0].select('td')[4].getText())
        availability.append(page.select('.product_page')[0].select('td')[5].getText())
        reviews.append(page.select('.product_page')[0].select('td')[6].getText())

data = {
    'title' : title,
    'category' : category,
    'upc' : upc,
    'product_type' : product_type,
    'price_excl' : price_excl,
    'price_incl' : price_incl,
    'tax' : tax,
    'availability' : availability,
    'no_of_reviews' : reviews
}

data = pd.DataFrame(data)
data.to_csv('book_data.csv', index = False)