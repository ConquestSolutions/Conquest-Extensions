##########
#
# STEP 9.1: THIS SCRIPT CHECKS IF THERE IS ANYTHING IN THE LOCATION FIELD, IF THERE IS IT WILL SEND A REQUEST TO THE GOOGLE GEOCOORDINATES API AND TRY AND RETRIEVE GEOCOORDINATES
# Copy this code into RequestInsertSaveValidation.
#
#NOTE: To test this, you'll need to save the script and then open up or add a new request.
#      Add some address values (like address, suburb, postcode etc) and watch it assign a location field with coordinates once you save the action.
#
##########

from System import *
from System.Windows import *

#generate first part of location by combining the other fields
Location = ''
if not String.IsNullOrWhiteSpace(source.Address):
	Location = str(source.Address) + ' \n'
if not String.IsNullOrWhiteSpace(source.Suburb):
	Location += str(source.Suburb) + ' \n'
if not String.IsNullOrWhiteSpace(source.PostCode):
	Location += str(source.PostCode) + ' \n'

#begin checking
if not String.IsNullOrWhiteSpace(Location):
	import urllib
	import urllib2
	import json
	
	#create API url to query
	googleMapsToken = "AIzaSyA-Jb5XWYjh5BqTUS6Feb-WtCDbhuoORJw"
	addressString = urllib.quote_plus(Location)
	url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + addressString + "&key=" + googleMapsToken
	print url
	
	#read the data and fetch the coordinates
	data = urllib2.urlopen(url).read()
	pyDict = json.loads(data)
	lat = pyDict['results'][0]['geometry']['location']['lat']
	lng = pyDict['results'][0]['geometry']['location']['lng']
	coordinates = str(lat) + ", " + str(lng)
	
	#if coordinates exist, append them to the Location
	if coordinates:		
		print coordinates
		Location += str(coordinates) + ' \n'
	
	#Generate the location field
	source.Location = Location