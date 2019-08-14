import requests
import json

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
body = ottawa_wards_response.json()

# Checking that the reponse has been requested correctly
print(body)
print('')


# Printing out the name of each ward
for i in range(len(body['objects'])):
    print(body['objects'][i]['name'])
print('')


# From the main API page, using the "federal-electoral-districts"
federal_post_office_response = requests.get('https://represent.opennorth.ca/postcodes/L5G4L3/?sets=federal-electoral-districts')
body = federal_post_office_response.json()

# Checking that the response has been requested correctly
print(body)
print('')
