import requests
from bs4 import BeautifulSoup

def parse_webpage(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        # Check the success of the request
        if response.status_code == 200:
            # Use BeautifulSoup to parse the HTML page
            soup = BeautifulSoup(response.text, 'html.parser')
            # Example: extract the title of the page
            title = soup.title.string
            print("Title:", title)
            # Example: extract all links on the page
            links = soup.find_all('a')
            print("Links:")
            for link in links:
                print(link.get('href'))
        else:
            print("Failed to fetch webpage. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    url = input("Enter URL to parse: ")
    parse_webpage(url)
