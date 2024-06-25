from modules.searchDownload import searchDownload
from modules.resizeImages import resizeImages
from modules.storeImages import storeImages
import asyncio
import time


if __name__ == '__main__': 
    query = input("Enter the query to search for: ")
    maximum = int(input("Enter the maximum number of pictures to download: "))

    print("Please wait...")

    asyncio.run(searchDownload(query, maximum)) # Runs in the asyncronous mode
    time.sleep(1)
    asyncio.run(resizeImages("Images", (150, 150))) # Runs in the asyncronous mode
    time.sleep(1)
    asyncio.run(storeImages("Images")) # Runs in the asyncronous mode