import argparse
import requests
from bs4 import BeautifulSoup

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error making request: {e}")
        return None

def print_response(response):
    if response:
        print(response)

def search(term):
    search_url = f"https://www.google.com/search?q={term}"
    response = make_request(search_url)
    if response:
        soup = BeautifulSoup(response, 'html.parser')
        results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
        for index, result in enumerate(results[:10], start=1):
            print(f"{index}. {result.get_text()}")

def main():
    parser = argparse.ArgumentParser(description="Make HTTP requests from the command line")
    parser.add_argument("-u", "--url", help="Make an HTTP request to the specified URL", metavar="<URL>")
    parser.add_argument("-s", "--search", help="Make an HTTP request to search the term using your favorite search engine", metavar="<search-term>")
    args = parser.parse_args()

    if args.url:
        print_response(make_request(args.url))
    elif args.search:
        search(args.search)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
