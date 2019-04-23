# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:14:27 2019

@author: xr293e
"""

tier1_city_list = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Agra', 'Ajmer', 'Aligarh',
                       'Amravati', 'Amritsar', 'Asansol', 'Aurangabad,Ahmedabad', 'Bareilly', 'Belgaum', 'Bhavnagar',
                       'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore',
                       'nagpur', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur', 'Erode',
                       'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon', 'Guwahati',
                       'Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar',
                       'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam',
                       'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai',
                       'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nanded', 'Nashik',
                       'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Prayagraj', 'PuneRaipur', 'Rajkot',
                       'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar',
                       'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli',
                       'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City',
                       'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']

def verifyLoc(loc):
    return False if loc.lower() not in [x.lower() for x in tier1_city_list] else True