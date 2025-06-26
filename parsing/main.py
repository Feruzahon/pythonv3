from bs4 import BeautifulSoup as bs
import requests

URL = 'https://www.kivano.kg/noutbuki?page='
products = []

def pars_page(url,count):
    response = requests.get(url+str(count))
    html = response.text
    soup = bs(html,'lxml')
    # print(soup)

    noutbuki = soup.find_all('div',class_='item product_listbox oh')
    
    # print(noutbuki)
    for noutbuk in noutbuki:
        title =noutbuk.find('div',class_ ='listbox_title oh').text
        image = 'www.kivano.kg'+ noutbuk.find('div',class_='listbox_img pull-left').find('img').get('src')
        price = noutbuk.find('div',class_= 'listbox_price text-center').text
        products.append({'title':title.replace('\n',''), 'image':image,'price':price.replace('\n','')})

    # print(products)

count = 1
while count !=20:
    pars_page(URL,count)
    print(count)
    count+=1




import json
with open ('products.json','w') as f:
    json.dump(products,f,ensure_ascii=False,indent=4)