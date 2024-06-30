#!/usr/bin/env python3
"""
By using the GitHub API, write a script that prints
the location of a specific user:
"""
import requests
import sys
import time

def main(url):
    """
    - The user is passed as first argument of the script
    with the full API URL, example: ./2-user_location.py
    https://api.github.com/users/holbertonschool
    - If the user doesn’t exist, print Not found
    - If the status code is 403, print Reset in X min where X
    is the number of minutes from now and the value of
    X-Ratelimit-Reset
    - Your code should not be executed when the file is
    imported (you should use if __name__ == '__main__':)
    """
    response = requests.get(url)

    if response.status_code == 404:
        print("Not found")
    elif response.status_code == 403:
        reset_timestamp = int(response.headers["X-Ratelimit-Reset"])
        current_timestamp = int(time.time())
        reset_in_minutes = (reset_timestamp - current_timestamp) // 60
        print("Reset in {} min".format(reset_in_minutes))
    else:
        user_data = response.json()
        location = user_data.get("location")
        if location:
            print(location)
        else:
            print("Location not available")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-user_location.py <GitHub API URL>")
        sys.exit(1)
    
    main(sys.argv[1])