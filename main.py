import requests
from datetime import datetime

USERNAME = 'yourusername'
TOKEN = 'yourtoken1'
GRAPH_ID = 'mygraph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Programing Graph',
    'unit': 'Hours',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

graph_new_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()

graph_new_pixel_config = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input('How many hours did you study today?'),
}

response = requests.post(url=graph_new_pixel_endpoint, json=graph_new_pixel_config, headers=headers)
print(response.text)

pixel_update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

pixel_update_config = {
    'quantity': '2',
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response)

pixel_delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)