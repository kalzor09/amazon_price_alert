import requests
import bs4
import re 

HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}
URL ="https://www.amazon.in/BassHeads-225-Super-Extra-Headphones/dp/B01M9C51T9/ref=sr_1_3?keywords=boat&qid=1564949899&s=gateway&sr=8-3"

#boat
def get_cost(url=URL,headers=HEADERS):
	res_boat = requests.get(url=url,headers=headers)
	soup = bs4.BeautifulSoup(res_boat.text,'html.parser')
	boat_cost_string = soup.find_all("div",{'id':'cerberus-data-metrics'})
	boat_cost = re.search(r'data\-asin\-price="(\d+)\.00"',str(boat_cost_string))
	# print(boat_cost.group(1))
	return boat_cost.group(1)


if __name__=="__main__":
	print(get_cost())