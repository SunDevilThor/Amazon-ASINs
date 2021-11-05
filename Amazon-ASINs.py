# Amazon ASINs from Search Page
# Tutorial from John Watson Rooney YouTube channel

from requests_html import HTMLSession

url = 'https://www.amazon.com/s?k=nvme+1tb'

s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1)

#print(r.html.find('title', first=True).full_text)

products = r.html.find('div[data-asin]')

asins = []

for item in products:
    if item.attrs['data-asin'] != '':
        asins.append(item.attrs['data-asin'])

print(asins)

# TO-DO: 
# For loop for each ASIN to get title of product
# Get price of each product