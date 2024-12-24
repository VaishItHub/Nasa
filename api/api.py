# import requests
# url='https://jsonplaceholder.typicode.com/posts'
# response=requests.get(url)
# if response.status_code==200:
#     print('data:', response.json())
# else:
#     print('data not found')


# it fect image and diplay

# import requests
# import webbrowser  # For opening the URL in a browser

# # Define the URL (Replace DEMO_KEY with your actual NASA API key)
# url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

# # Send a GET request
# response = requests.get(url)

# # Check the response status
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()

#     # Extract the image URL
#     image_url = data.get('url', None)

#     if image_url:
#         print(f"Opening image: {image_url}")
#         # Open the image URL in the default web browser
#         webbrowser.open(image_url)
#     else:
#         print("Image URL not found in the response.")
# else:
#     print('Data not found')

# to store that image
import requests

# Define the URL (Replace DEMO_KEY with your actual NASA API key)
url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

# Send a GET request
response = requests.get(url)

# Check the response status
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the image URL
    image_url = data.get('url', None)

    if image_url:
        print(f"Downloading image from: {image_url}")
        
        # Send a GET request to the image URL
        image_response = requests.get(image_url)
        
        # Check if the image request was successful
        if image_response.status_code == 200:
            # Save the image to a file
            with open("nasa_image.jpg", "wb") as file:
                file.write(image_response.content)
            print("Image saved successfully as nasa_image.jpg")
        else:
            print("Failed to download the image.")
    else:
        print("Image URL not found in the response.")
else:
    print('Data not found')
