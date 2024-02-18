from dputils.scrape import Scraper, Tag
from database import Product, save_product, opendb

sc = Scraper('https://digipodium.com/mining-demo.html')
result = sc.get_repeating_page_data(
    target=Tag(cls='item-list'),
    items= Tag(cls='col'),
    name = Tag('h4'),
    price = Tag('h1'),
    discount = Tag('li', cls='discount'),
    oprice = Tag('li', cls='o-price'),
    sold = Tag('li', cls='total-bought'),
    qty = Tag('li', cls='left'),

 )
#cleaning the data
clean_results = []
for row in result:
    price = float(row['price'][1:])
    discount = float(row['discount'].lower().replace('% discount',''))
    oprice = float(row['oprice'][1:])
    sold = int(row['sold'].split()[0])
    qty = int(row['qty'].split()[0])
#     clean_results.append({
#         'name': row['name'],
#         'price': price,
#         'discount': discount,
#         'oprice': oprice,
#         'sold': sold,
#         'qty': qty
#     })
# print(clean_results)
 # save to bd
save_product(
    opendb(),
    Product(
        name = row['name'],
        price = price,
        discount = discount,
        oprice = oprice,
        sold = sold,
        qty = qty
    )
)
print(f'{row["name"]} added to db')   