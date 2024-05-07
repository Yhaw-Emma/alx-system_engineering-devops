#!/usr/bin/python3

"""Function to query subcribers on a given Reddit subreddit"""
import requests

def number_of_subscribers(subreddit):
   
    # URL for the subreddit's information endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent header to avoid 429 errors
    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    
    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        
        # Extract number of subscribers from the response
        subscribers = data['data']['subscribers']
        
        return subscribers
    else:
        # If subreddit is invalid or another error occurred, return 0
        return 0