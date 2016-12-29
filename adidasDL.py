#!/usr/bin/python
import urllib, urllib2, threading
#BB4677 - triple black ultraboosts
#S77416 - triple white ultraboosts
#AQ2660 - moon rock yeezy 350
#BB1839 - pirate black yeezy 750
#S79168 - red blue white nmd primeknit
#S79478 - grey camo/oreo nmd r1 primeknit
#BA8597 - olive nmd primeknit
#BA8630 - white nmd primeknit

#List of prepended letters of style code - add new strings here
styleCodeChar=['BB', 'BA', 'AQ', 'CP', 'S']

def redirect(prefix):
	"""
	Prints redirect of style code's produt page
	Attempts to then print the image using said style code (could implement url check on produyct page for image prelim check)

	:params prefix: string the letters prepended to the style code
	"""
	if len(prefix)==2:
		start=1000
		end=9999
	elif len(prefix)==1:
		start=10000
		end=99999
	while start<end+1:
		count=start
		url='http://www.adidas.com/us/adidas-/'+prefix+str(count)+'.html'
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36')
		req.add_header('Accept-Language','en-US,en;q=0.8')
		req.add_header('Connection','keep-alive')
		req.add_header('Accept-Encoding','gzip,deflate,sdch')
		res = urllib2.urlopen(req)
		redirectResult = res.geturl()
		try:
			res = urllib2.urlopen("http://demandware.edgesuite.net/sits_pod20-adidas/dw/image/v2/aaqx_prd/on/demandware.static/Sites-adidas-US-Site/Sites-adidas-products/en_US/v1460455685655/zoom/"+prefix+str(count)+"_01_standard.jpg?sw=500&sfrm=jpg")
			if res.getcode() == 200:
				print prefix+str(count)+' - '+redirectResult				
				urllib.urlretrieve("http://demandware.edgesuite.net/sits_pod20-adidas/dw/image/v2/aaqx_prd/on/demandware.static/Sites-adidas-US-Site/Sites-adidas-products/en_US/v1460455685655/zoom/"+prefix+str(count)+"_01_standard.jpg?sw=500&sfrm=jpg", "images/"+prefix+str(count)+".jpg")
		except Exception as e:
			print prefix+str(count)+' - '+str(e)
		start+=1

if __name__ == '__main__':
	"""
	Main slots controller
	"""
	for prefix in styleCodeChar:
		print prefix, 'Thread initialized!'
		t = threading.Thread(target=redirect, args=(prefix,))
		t.start()