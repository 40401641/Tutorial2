import urllib2, json, base64
accesstoken = "0TZQ9JN05XBNCG52M5YC"
#accesstoken = "0TZQ9JN05XBNCG52M5TT"
url = "http://data.unistats.ac.uk/api/v4/KIS/Institutions.json"
#url = "http://data.unistats.ac.uk/api/v4/KIS/Binstitution .json"
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
#request.add_header(
#	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
#	)

response = urllib2.urlopen(request)
data = json.load(response)
for c in data:
	print c['UKPRN'], c['Name']
