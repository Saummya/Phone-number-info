# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 19:59:22 2021

@author: saumy
"""

# Program to find carrier and region
# of a phone number
import phonenumbers
from phonenumbers import geocoder, carrier
  
# Parsing String to Phone number
phoneNumber = phonenumbers.parse("+916203810580")
  
# Getting carrier of a phone number
Carrier = carrier.name_for_number(phoneNumber, 'en')
  
# Getting region information
Region = geocoder.description_for_number(phoneNumber, 'en')
  
# Printing the carrier and region of a phone number
print(Carrier)
print(Region)