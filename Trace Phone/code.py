import phonenumbers as PN

from phonenumbers import timezone, geocoder, carrier

user_phone_number = input("Enter your phone number with +__ : ")

phone_details = PN.parse(user_phone_number)

time = timezone.time_zones_for_number(phone_details)

vendor = carrier.name_for_number(phone_details, "en")

registrer = geocoder.description_for_number(phone_details, "en")

print(user_phone_number)
print(time)
print(vendor)
print(registrer)

