#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        json_str = r.json()
        if len(json_str) == 0:
            print("No result")
        else:
            result = json_str.get('id')
            print("[{}] {}".format(json_str.get('id'), json_str.get('name')))
    except:
        print("Not a valid JSON")
