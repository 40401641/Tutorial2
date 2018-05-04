import urllib2, json, base64
accesstoken = "0TZQ9JN05XBNCG52M5YC"
institution = "10007772"
course = "U56119"
page = 0
url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
	institution,
	course
	)
request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response = urllib2.urlopen(request)
data = json.load(response)
#print json.dumps(data,indent=2)
for c in data:
    if c["Code"] == "SALARY":
        d = c["Details"]
        for b in d:
            if b["Code"] == "MED":
                print (b["Value"])
                
for c in data:
    if c["Code"] == "SALARY":
        d = c["Details"]
        for b in d:
            if b["Code"] == "LDMED":
                print (b["Value"])
            
for c in data:
    if c["Code"] == "NSS":
        d = c["Details"]
        for b in d:
            if b["Code"] == "Q1":
                print (b["Value"])
