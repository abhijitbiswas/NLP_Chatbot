from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import verifyLocation
from email.message import EmailMessage
import smtplib

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		
		if loc is None:
			dispatcher.utter_message("-----"+"Please choose correct location")
			return [SlotSet('location',None)]            
		if verifyLocation.verifyLoc(loc) is False:
			dispatcher.utter_message("-----"+"Zommato do not have service in this Location: ")
			return [SlotSet('location',None)]
			
		cuisine = tracker.get_slot('cuisine')
		budget_1 = 0
		budget_2 = 100000
		
		print("budget_range::::",budget_1, budget_2)
		if tracker.get_slot('budget_1') is not None:
			budget_1 = int(tracker.get_slot('budget_1'))
		if tracker.get_slot('budget_2') is not None:
			budget_2 = int(tracker.get_slot('budget_2'))
			
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			index=0
			for restaurant in d['restaurants']:				
				if((budget_1 <= restaurant['restaurant']['average_cost_for_two'] <= budget_2) & index <= 5):
					index= index+1
					response=response+ "\nFound \n"+ restaurant['restaurant']['name']+" In "+ restaurant['restaurant']['location']['address']+" has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']
			if(index == 0):
				response= response+"\n No restaurant found in given preferance"
				return
						
		dispatcher.utter_message("-----"+response)
		return [SlotSet('response',d)]

#Action class for To send detail mail to client
class SendDetailMailToClient(Action):
	def name(self):
		return 'send_detail_mail'
		
	def run(self, dispatcher, tracker, domain):
		email= tracker.get_slot("email")
		#Email send service API call
		budget_1 = 0
		budget_2 = 100000
		
		print("budget_range::::",type(budget_1), type(budget_2))
		if tracker.get_slot('budget_1') is not None:
			budget_1 = int(tracker.get_slot('budget_1'))
		if tracker.get_slot('budget_2') is not None:
			budget_2 = int(tracker.get_slot('budget_2'))
		
		d = tracker.get_slot('response')
		index=0
		response=""
		for restaurant in d['restaurants']:				
			if((budget_1 <= restaurant['restaurant']['average_cost_for_two'] <= budget_2) & index <= 10):
				index= index+1
				response=response+ "\nName::"+ restaurant['restaurant']['name']+" \nAddress::"+ restaurant['restaurant']['location']['address']+"\n Average Budget for Two People::"+restaurant['restaurant']['average_cost_for_two']+" \nZomato user rating "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
		if(index == 0):
			response= response+"\n No restaurant found in given preferance"
		
		email_from="teamrestro@gmail.com"
		email_from_login_pwd ="passwordlogin"
		email_content=response
		email_subject="Resturent search result"
		self.send_email_to_client(email,email_from,email_content,email_subject,email_from_login_pwd)
		dispatcher.utter_message("Email sent successfully")
		return
    
	def send_email_to_client(self,to_send,email_from,email_content,email_subject,email_from_login_pwd):
		msg = EmailMessage()
		msg['Subject'] = email_subject
		msg['From'] = email_from
		msg['To'] = to_send
		msg.set_content(email_content)
		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()
		mail.starttls()
		login_id = msg['From']
		login_pwd = email_from_login_pwd
		mail.login(login_id, login_pwd)
		mail.sendmail(msg['From'], msg['To'], msg.get_content())


#Action class to Verify Location for restaurant search
class ActionVerifyLocation(Action):
	def name(self):
		return 'verify_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		loc2= tracker.latest_message.text
		print("location",loc,loc2)
		if loc is None:
			dispatcher.utter_message("-----"+"Please choose correct location")
			return [SlotSet('location',None)]            
		if verifyLocation.verifyLoc(loc) is False:
			dispatcher.utter_message("-----"+"Zommato do not have service in this Location: ")
			return [SlotSet('location',None)]
        
		return [SlotSet('location',loc.lower())]