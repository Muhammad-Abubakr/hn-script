import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')	## html.parser gives us an html doc instead of string which we can than manipulate
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_Stories_by_points(hnlist):
	return sorted(hnlist,key= lambda k:k['votes'] ,reverse=True)

def custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href')
		vote = subtext[idx].select('.score')
		if len(vote):	
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
						hn.append({'title':title, 'href': href, 'votes':points})

	return sort_Stories_by_points(hn)


pprint.pprint(custom_hn(links, subtext))