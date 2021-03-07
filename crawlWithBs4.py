import requests,bs4
res = requests.get('https://en.wikipedia.org/wiki/Steve_Jobs')
playFile=open('stevejobs.html', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)
soup = bs4.BeautifulSoup(open('stevejobs.html'),'html.parser')
spanElem = soup.select('h1#firstHeading')[0]
print(spanElem.getText())
