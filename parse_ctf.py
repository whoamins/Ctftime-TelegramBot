import requests
import json

from bs4 import BeautifulSoup


class Parser:
	def __init__(self):
		self.headers = {
		    "Accept": "*/*",
		    "User-Agent": "Mozilla/4.0 (Windows NT 7.0; Win86; x86; rv:82.0) Gecko/201110101 Firefox/77.0"
		}
  	

	def get_ctf_list(self):
		url = "https://ctftime.org/event/list/upcoming"

		req = requests.get(url, headers=self.headers)

		soup = BeautifulSoup(req.text, 'lxml')

		all_ctfs = soup.find('table', class_="table").find_all('a')

		all_ctfs_list = []

		for ctf in all_ctfs:
		    ctf_name = ctf.text
		    ctf_link = f"https://ctftime.org{ctf.get('href')}"
		    ctf_info = f"{ctf_name} | {ctf_link}"
		    all_ctfs_list.append(ctf_info)


		result = ""
		for item in all_ctfs_list:
			result += f'{item}\n'

		return result


	def get_next_ctf(self):
		url = "https://ctftime.org/event/list/upcoming"

		req = requests.get(url, headers=self.headers)

		soup = BeautifulSoup(req.text, 'lxml')

		next_ctf = soup.find('table', class_='table').find('a')
		next_ctf_time_obj = soup.find('table', class_='table').find_all('tr')
		next_ctf_time = next_ctf_time_obj[1].find('td').find_next('td').text

		ctf_link = f"https://ctftime.org{next_ctf.get('href')}"

		return f"{next_ctf.text} | {next_ctf_time} | {ctf_link}"



	def get_idcz_rank(self):
		url = 'https://ctftime.org/team/144064'

		req = requests.get(url, headers=self.headers)

		soup = BeautifulSoup(req.text, 'lxml')

		overall_rating_place = soup.find('div', class_='tab-pane active', id='rating_2021').find('b').text

		country_place = soup.find('div', class_='tab-pane active', id='rating_2021').find('b').find_next('a').text

		info = f'Общий топ: {overall_rating_place.strip()} | Россия: {country_place.strip()}'

		return info 