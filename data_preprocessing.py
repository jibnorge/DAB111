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
