import requests

def get_suggestions(query):

    url = f"https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={query}"

    r = requests.get(url).json()

    return r[1]
