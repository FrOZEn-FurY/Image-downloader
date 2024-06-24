from modules.searchDownload import searchDownload
from modules.resizeImages import resizeImages
import asyncio
import time


if __name__ == '__main__': 
    query = input("Enter the query to search for: ")
    maximum = int(input("Enter the maximum number of pictures to download: "))

    print("Please wait...")

    asyncio.run(searchDownload(query, maximum))
    time.sleep(1)
    asyncio.run(resizeImages("Images", (150, 150)))