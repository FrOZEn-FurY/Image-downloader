# from simple_image_download import simple_image_download as simp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

async def searchDownload(query, maximum):
    options = Options()
    options.add_argument("--headless") # A headless browser does not open up a browser window
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled") # These two lines prevent the browser from crashing
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # Install the latest version of ChromeDriverManager
    driver.maximize_window() # Maximize the browser window (not required)

    driver.get(f"https://www.google.com/search?hl=en&tbm=isch&q={query}") # Search for the query

    time.sleep(3) # Wait so the pictures get loaded

    if not os.path.exists("Images"): # Making the directory if not exists
        os.mkdir("Images")

    cntr = 0

    images = driver.find_elements(By.TAG_NAME, "img") # Finding all the images
    for image in images[50:]:
        if cntr == maximum:
            break
        try:
            image.screenshot(f"Images/{cntr}.png") # Taking an screenshot from them and store them in a file.
            cntr += 1
            print(f"Downloaded {cntr} images.")
        except:
            print("Could not resolve the image.")

    driver.quit()


# The simple_image_download method is deprecated.
# async def searchDownload(query, maximum):
#     try:
#         downloader = simp.simple_image_download()
#         downloader.download(query, limit=maximum)
#         if not os.path.exists("Images"): # Making the directory if not exists
#             os.mkdir("Images")
#         for file in os.listdir(f'simple_images/{query}'):
#             os.rename(os.path.join(query, file), os.path.join("Images", file))
#         os.rmdir(query)
#         print("Images downloaded successfully!")
#     except Exception as e:
#         print(f"Error: {e}")

