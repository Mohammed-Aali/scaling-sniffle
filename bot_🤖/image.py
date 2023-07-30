import requests
import keys


# Define the access key
access_key = keys.unsplash_api

# Define the API endpoint
endpoint = "https://api.unsplash.com/photos?"
# Define the query parameters
params = {
  "query": "nature", # The search term
  "orientation": "landscape", # The photo orientation
  "count": 1, # The number of photos to return "auto": 'format',
  "auto": 'format'
}

# Send a GET request to the endpoint with the access key and parameters
response = requests.get(endpoint, params=params, headers={"Authorization": "Client-ID {}".format(access_key)})
# Check if the request was successful
if response.status_code == 200:
  # Parse the JSON response
    data = response.json()
    print(data[0])
    
    # Get the first photo in the list
    photo = data[0]

    # Print some information about the photo
    print("Photo ID: {}".format(photo["id"]))
    print("Photo URL: {}".format(photo["urls"]["regular"]))
    print("Photographer: {}".format(photo["user"]["name"]))

    response_1 = requests.get("https://api.unsplash.com/photos/VLpRa5tFdNY/download", params=params, headers={"Authorization": "Client-ID {}".format(access_key)})
    response_1 = response_1.json()
    print(f'Download url: {response_1}')
else:
  # Print an error message
  print("Request failed with status code {}".format(response.status_code))


