#!/usr/bin/python3
"""This script queries the Reddit API and returns the number of total
subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the
        request fails or the subreddit does not exist.
    """
    # Construct the URL for the Reddit API request
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Send a GET request to the API to retrieve the number of subscribers
    response = requests.get(
        url,
        allow_redirects=False,
        headers={"user-agent": "nabuntu_bot-01"},
        timeout=60,
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the number of subscribers from the response JSON
        subscribers = response.json()["data"]["subscribers"]
        return subscribers
    else:
        # Return 0 if the request failed or the subreddit does not exist
        return 0
