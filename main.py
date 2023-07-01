import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = 'ryan0909090909'
TOKEN = 'habit_tracking'
GRAPH_ID = 'graph-start'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'sora'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
print(today.strftime('%Y %m %d'))

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs{GRAPH_ID}"
pixel_data = {
    "data": today.strftime('%Y*%m*%d'),
    "quantity": input('how many km did you cycle today????')
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# how to use HTTP Put and Delete Requests
# put: update
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs{GRAPH_ID}/{today.strftime('%Y %m %d')}"
new_pixel_data = {
    'quantity': '5'
}
# response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)

# delete a pixel
pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs{GRAPH_ID}/{today.strftime('%Y %m %d')}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)