import requests
from bs4 import BeautifulSoup
import json

class Atbmarket_promotions:
	@staticmethod
	def get_atb_promotions():
		page = requests.get('https://www.atbmarket.com/hot/akcii/economy')
		soup = BeautifulSoup(page.content)

		info = soup.find_all('div', class_ = 'promo_info')
		result = []

		for i in info:
			product_name = i.find('span', class_ = 'promo_info_text').get_text(strip=True) 

			try:						#not all products have old price
				old_price = i.find('span', class_ = 'promo_old_price').get_text(strip=True)
			except AttributeError:
				old_price = ''

			new_price = i.find('div', class_ = 'promo_price').get_text(strip=True)
			np = new_price[-5:]		#I add a point and formatting the price
			new_price = new_price[0:-5]
			new_price += '.' + np[:2]

			try:						#not all products have percent of discount
				discount = i.find('div', class_ = 'economy_price').get_text(strip=True)
				discount = discount.replace('Економія-', '')
			except:
				discount = ''

			info_dict = {
				'productName': product_name,
				'oldPrice': old_price,
				'newPrice': new_price,
				'discount': discount
				}

			if info_dict not in result:		#I discard the copies
				result.append(info_dict)

		return result