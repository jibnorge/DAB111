import pandas as pd

data = pd.read_csv('book_data.csv')
data.head()

# data['title'][0].split('|')[0].split('\n')[1].strip()
data['title'] = [i.split('|')[0].split('\n')[1].strip() for i in data['title']]

data['price_excl'] = [i.strip('Â£') for i in data['price_excl']]
data['price_excl'] =  data['price_excl'].astype('float')

data['price_incl'] = [i.strip('Â£') for i in data['price_incl']]
data['price_incl'] =  data['price_incl'].astype('float')

data['tax'] = [i.strip('Â£') for i in data['tax']]
data['tax'] =  data['tax'].astype('float')

data['stock_availability'] = [i.split('(')[0].strip() for i in data['availability']]
data['available_count'] = [i.split('(')[1].split()[0] for i in data['availability']]
data.drop(columns = 'availability', inplace = True)
data['available_count'] = data['available_count'].astype('int')

data.to_csv('books_updated.csv', index = False)

features = pd.DataFrame({"Features" : data.columns})

features['Description'] = ["The title of the book", 
                        "The genre to which the book belongs", 
                        "A unique identifier for the book", 
                        "Type of the product", 
                        "The price of the book excluding any taxes", 
                        "The total price of the book, including taxes", 
                        "The amount of tax applied to the book", 
                        "The number of reviews the book has received", 
                        "Indicates whether the book is in stock or not", 
                        "The number of copies available in stock"]

features.to_csv('features.csv', index = False)
