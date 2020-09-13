# Created for Code For Atlanta on the National Day of Civic Hacking 2020
# By Ross Llewallyn

# pip install these if necessary
import requests
from bs4 import BeautifulSoup

# Get food pantry information from this great site!
base_site = "https://www.foodpantries.org/ci/"
loc_path = "ga-atlanta"

page = requests.get(base_site + loc_path)

# Check if successfully retrieved
if page.status_code == 200:
	soup = BeautifulSoup(page.content, 'html.parser')
	#print(soup.prettify())

	# Get panty element list
	names = soup.find_all("h2")

	pantries = {}

	for t in names:
		# TODO: Go into details page to find more information
		name = t.get_text().strip()

		# foodpantries.org link, not their website (available in details page)
		url = t.find("a")["href"]

		# Next div has class "nailthumb-container": could use as additional selector
		img_div = t.findNext("div")
		img = img_div.find("img")["src"]

		# City + ZIP; phone number
		info_p = img_div.findNext("p")
		# Info not in separate elements - raw text between breaks
		info = str(info_p).split("<br/>")[1:3]
		for i in range(len(info)):
			# Strip left and right to handle line endings
			info[i] = info[i].lstrip().rstrip()

		loc_rough = info[0]
		phone = info[1]

		# Remaining description text
		descr_p = info_p.findNext("p")
		descr = descr_p.get_text().strip()

		pantries[name] = {
			"name": name,
			"link": url,
			"image": img,
			"loc_rough": loc_rough,
			"phone": phone,
			"descr": descr,
		}
else:
	print("Could not access page: " + site)

# Show results
print(pantries)