""" raddit api"""


import json
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """Count occurrences of given keywords in hot articles recursively."""
    if after is None:
        word_count = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    headers = {'User-Agent': 'bhalut'}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        after_data = data.get("after")
        
        for post in data.get("children"):
            title = post.get("data").get("title").lower()
            for word in word_list:
                if word.lower() in title.split():
                    word_count[word.lower()] += 1

        if after_data:
            count_words(subreddit, word_list, after=after_data, word_count=word_count)
        else:
            print_results(word_count)

def print_results(word_count):
    """Print the word count in descending order by count and ascending order by word."""
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print(f"{word}: {count}")