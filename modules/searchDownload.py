from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

async def searchDownload(query, maximum):
    options = Options()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()

    driver.get(f"https://www.google.com/search?hl=en&tbm=isch&q={query}")

    time.sleep(3)

    if not os.path.exists("Images"):
        os.mkdir("Images")

    cntr = 0

    images = driver.find_elements(By.TAG_NAME, "img")
    for image in images[50:]:
        if cntr == maximum:
            break
        try:
            image.screenshot(f"Images/{cntr}.png")
            cntr += 1
            print(f"Downloaded {cntr} images.")
        except:
            print("Could not resolve the image.")

    driver.quit()
