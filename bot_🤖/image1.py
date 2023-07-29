import requests
import sys
import keys

def main():
    data = get_image_data(keys.unsplash_api, 'nature')
    print(f'The type of data is: {type(data)} \n')
    print('The Data \n{}'.format(data))

    download_img(keys.unsplash_api, data)




def get_image_data(access_key: str, query: str, count: int=1):
    # Define the query parameters
    params = {
    "query": query, # The search term
    "orientation": "landscape", # The photo orientation
    "count": count, # The number of photos to return,
    "auto": "format"
    }
    response = requests.get('https://api.unsplash.com/photos/random?client_id={}'.format(access_key), params=params)

    if response.status_code == 200:
        return response.json()[0]
    else:
        print("Request failed with status code {}".format(response.status_code))
    
    return response.json()

def download_img(access_key: str, img_data, img_name: str='image.jpg'):
    response = requests.get(img_data['links']['download_location'], {'client_id': access_key})

    if response.status_code != 200:
        sys.exit('Request for triggering download failed with status code {}'.format(response.status_code))

    img = requests.get(img_data["urls"]["raw"])
    image = img.content

    with open(img_name, 'wb') as f:
        f.write(image)
    

if __name__ == '__main__':
    main()