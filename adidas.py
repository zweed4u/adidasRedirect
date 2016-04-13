#!/usr/bin/env python
import urllib2
#BB4677 - triple black ultraboosts
#S77416 - triple white ultraboosts
#AQ2660 - moon rock yeezy 350
#BB1839 - pirate black yeezy 750
#S79168 - red blue white nmd primeknit
#S79478 - grey camo/oreo nmd r1 primeknit
#BA8597 - olive nmd primeknit
#BA8630 - white nmd primeknit
#check finds here:
#http://demandware.edgesuite.net/sits_pod20-adidas/dw/image/v2/aaqx_prd/on/demandware.static/Sites-adidas-US-Site/Sites-adidas-products/en_US/v1460455685655/zoom/BB1970_01_standard.jpg?sw=500&sfrm=jpg

styleCodeChar=raw_input('Stylecode prefix? (eg. BB, BA, S, AQ) ')
start=int(raw_input('Starting number? '))
end=int(raw_input('Ending number? '))
count=start

def redirect(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36')
	req.add_header('Accept-Language','en-US,en;q=0.8')
	req.add_header('Connection','keep-alive')
	req.add_header('Accept-Encoding','gzip,deflate,sdch')
	res = urllib2.urlopen(req)
	redirectResult = res.geturl()
	print styleCodeChar+str(count)+' - '+redirectResult

while count<end:
	try:
		redirect('http://www.adidas.com/us/adidas-/'+styleCodeChar+str(count)+'.html')
	except:
		print styleCodeChar+str(count)
	count+=1
