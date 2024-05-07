#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""

import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct URL for querying the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set custom User-Agent header to avoid 429 errors
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    
    # Parameters to limit the number of posts to 10
    params = {"limit": 10}
    
    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the subreddit is valid
    if response.status_code == 200:
        # Parse JSON response
        data = response.json().get("data")
        
        # Extract and print titles of the first 10 hot posts
        for post in data.get("children"):
            print(post.get("data").get("title"))
    else:
        # If subreddit is invalid, print None
        print(None)
