from flask import Flask, redirect, url_for, request
import googlemaps
from googleplaces import GooglePlaces, types, lang

app = Flask(__name__)

# @app.route('/')
# def main():
# 	return "Welcome!"

def get_places():
	gmaps = googlemaps.Client(key='AIzaSyCBosCz9uWd0isSI2WOsQCS1e607_AQTqI')
	google_places = GooglePlaces('AIzaSyCBosCz9uWd0isSI2WOsQCS1e607_AQTqI')

	# Geocoding an address
	geocode_result_a = gmaps.geocode(input())
	geocode_result_b = gmaps.geocode(input())


	#find where Hannan is
	hannan_lat = (geocode_result_a[0]['geometry']['location']['lat'])
	hannan_lng = (geocode_result_a[0]['geometry']['location']['lng'])

	#find where David is
	david_lat = (geocode_result_b[0]['geometry']['location']['lat'])
	david_lng = (geocode_result_b[0]['geometry']['location']['lng'])

	#find midpoint between David and Hannan
	avg_distance_lat = (hannan_lat + david_lat)/2
	avg_distance_lng = (hannan_lng + david_lng)/2

	#look up nearby shops that are equidistant 
	query_result = google_places.nearby_search(lat_lng= {"lat": avg_distance_lat, "lng": avg_distance_lng}, radius=300, types=[types.TYPE_FOOD])
	names = [place.name for place in query_result.places]
	# for place in query_result.places:
	#     print(place.name)
	return "<br/>".join(names[0:5])
	# return query_result.places


@app.route("/")
def hello():
    return get_places()

if __name__ == "__main__":
	app.run()

 