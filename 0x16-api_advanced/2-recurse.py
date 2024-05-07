#!/usr/bin/python3
"""
Using reddit's API
"""

import requests

def recurse(subreddit, after=None, hot_list=[]):
    """Return top ten post titles recursively."""
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    
    # Send GET request to the Reddit API
    results = requests.get(url, params=parameters, headers=user_agent, allow_redirects=False)
    
    # Check if the request was successful
    if results.status_code == 200:
        data = results.json().get("data")
        
        # Extract 'after' token for pagination
        after_data = data.get("after")
        
        # Recursively call the function with the next 'after' token
        if after_data is not None:
            recurse(subreddit, after=after_data, hot_list=hot_list)
        
        # Extract titles of hot posts from the current page
        all_titles = data.get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        
        return hot_list
    else:
        # If subreddit is invalid or another error occurred, return None
        return None
