import zomatopy
import json
import verifyLocation 
def test():
	config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
	zomato = zomatopy.initialize_app(config)
	loc = 'Bangalore'
	cuisine = 'Nort Indian'
	budget_1 = 0
	budget_2 = 1500
	location_detail=zomato.get_location(loc, 1)
	d1 = json.loads(location_detail)
	lat=d1["location_suggestions"][0]["latitude"]
	lon=d1["location_suggestions"][0]["longitude"]
	cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
	results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 10)
	d = json.loads(results)
	response=""
	if d['results_found'] == 0:
		response= "no results"
	else:
		index=0
		for restaurant in d['restaurants']:
			print(restaurant['restaurant']['average_cost_for_two'])
			if((budget_1 <= restaurant['restaurant']['average_cost_for_two'] <= budget_2) & index <= 5):
				index= index+1
				response=response+ "\nFound \n"+ restaurant['restaurant']['name']+" In "+ restaurant['restaurant']['location']['address']+" has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']
		if(index == 0):
			response= response+"\n No restaurant found in given preferance"
			
		
	print(response)

test()
    
if verifyLocation.verifyLoc("Bangalore") is False:
    print("Not Found")
else:
    print("Found")