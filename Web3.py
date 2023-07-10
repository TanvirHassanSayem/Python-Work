import urllib2, bs4

url = "http://kafemud.bilkent.edu.tr/monu_tr.html"
req = urllib2.urlopen(url)
raw = req.read()
soup = bs4.BeautifulSoup(raw)

print (soup.prettify().encode('utf-8'))