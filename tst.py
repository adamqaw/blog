# from news import News
#
# n = News()
#
# print(n.article_urls)


from stock import Stock
from datetime import date

# s = Stock('AAPL', '2022-02-14', 'true')
# print(s.get_stock())

day = date.today().strftime('%Y-%m-%d')
print(day)
