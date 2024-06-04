#!/usr/bin/python3
""" module for function to return top 10 hot posts of a given subreddit """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of all hot articles for a given subreddit.

    Args:
        subreddit: The name of the subreddit.
        hot_list: The list of hot titles to append to.

    Returns:
        list: The list of titles of all hot articles for the subreddit,
        or None if the queried subreddit is invalid.
    """
    global after

    # Set the headers for the HTTP request
    headers = {'User-Agent': 'xica369'}

    # Construct the URL for the Reddit API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set the parameters for the Reddit API request
    parameters = {'after': after}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        # Extract the "after" parameter from the response JSON
        next_ = response.json().get('data').get('after')

        # If there are more hot articles, recursively call the function
        if next_ is not None:
            after = next_
            return recurse(subreddit, hot_list)

        # Extract the titles of the hot articles from the response JSON
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))

        # Return the list of hot article titles
        return hot_list
    else:
        # Return None if the request failed
        return None
