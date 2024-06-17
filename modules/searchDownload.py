import requests

async def searchDownload(query, maximum):
    url = 'https://www.google.com/search' # The root url.
    params = {
        'q': query,
        'tbm': 'isch'
        # Using query given and also the tbm param which searchs the images.
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        # It is just mimicing a real browser.
    }

    try:
        response = await requests.get(url, params=params, headers=headers)
        if response.status_code == 200: # Checking the status of the request
            return response.text
        else:
            print(f"Error in fetching the data with status code '{response.status_code}'")
            return None
    except requests.RequestException as e: # If any other errors happened beside the status codes
        print(f"Error occured '{e}'")
        return None