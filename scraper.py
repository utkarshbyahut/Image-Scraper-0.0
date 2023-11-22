from typing_extensions import Concatenate
import requests
from bs4 import BeautifulSoup
import os

# Specify the target URL to scrape images from
url = 'https://unsplash.com/'  # Replace with the target website URL

# Send a GET request to the URL
response = requests.get(url)

print(f"{url} Responded With Code :", response.status_code)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    with open ("/content/drive/My Drive/Projects/Image_Scraper/websitedata.txt", 'w+') as wbd:
      images = soup.find_all('img')
      img_count = 1
      for image in images:
        img_url = image['src']

        if (img_url[0] == "h"):
          wbd.write(f"Image url {img_count} :")
          wbd.write(img_url)
          wbd.write('\n')
          img_count += 1

        else:
          continue

    # Create a directory to save the images
    if not os.path.exists('/content/drive/My Drive/Projects/Image_Scraper/scraped_images_3'):
        os.makedirs('/content/drive/My Drive/Projects/Image_Scraper/scraped_images_3')

    # Download and save the images
    with open ('/content/drive/My Drive/Projects/Image_Scraper/websitedata.txt', 'r+') as wbd:
      img_count = 1
      for image in wbd:
        img_url_index = (image.strip()).find('h')
        img_url = ((image.strip())[img_url_index::])
        print(img_url)
        img_count += 1

        if(requests.get(img_url).content):
          img_data = requests.get(img_url).content
          img_name = f"Image {img_count}"
          with open(f'/content/drive/My Drive/Projects/Image_Scraper/scraped_images_3/{img_name}', 'wb') as f:
              f.write(img_data)
              print(f'Saved {img_name}')
