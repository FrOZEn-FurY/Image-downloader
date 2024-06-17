from .modules.searchDownload import searchDownload
import asyncio


if __name__ == '__main__': 
    query = input("Enter the query to search for: ")
    maximum = int(input("Enter the maximum number of pictures to download: "))

    text = asyncio.run(searchDownload(query, maximum))

    print(text)
