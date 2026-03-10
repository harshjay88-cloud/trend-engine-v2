import requests

def get_trending_videos():

    url = "https://www.googleapis.com/youtube/v3/videos"

    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": "US",
        "maxResults": 25,
        "key": "YOUR_API_KEY"
    }

    r = requests.get(url,params=params)

    return r.json()
