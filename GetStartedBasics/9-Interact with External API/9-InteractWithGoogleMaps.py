from System import *
from System.Windows import *

import urllib
import urllib2
import json

googleMapsToken = "AIzaSyA-Jb5XWYjh5BqTUS6Feb-WtCDbhuoORJw"
piggy = urllib.quote_plus("7 Arnold st Parkside sa 5063")
url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + piggy + "&key=" + googleMapsToken
print url

data = urllib2.urlopen(url).read()
pyDict = json.loads(data)
lat = pyDict['results'][0]['geometry']['location']['lat']
long = pyDict['results'][0]['geometry']['location']['lng']
print str(lat) + ", " + str(long)