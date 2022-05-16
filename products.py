# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:45:54 2022

@author: jenny
"""
products = []

while True:
    name = input('請輸入產品名稱: ')
    if name == 'q':
        break;
    price = input('請輸入產品價格: ')
    #p = []
    #p.append(name)
    #p.append(price)
    #p = [name , price]
    products.append([name, price])
print(products)
        