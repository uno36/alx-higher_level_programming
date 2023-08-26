#!/usr/bin/python3
"""
Python script that takes in a string and sends a search request
to the Star Wars API
"""
if __name__ == "__main__":
    import requests
    import sys

    try:
        q = sys.argv[1]
    except IndexError:
        q = ""

    r = requests.get('https://swapi.co/api/people/?search={}'.format(q))
    try:
        json_str = r.json()
        if len(json_str) == 0:
            print("No result")
        else:
            results = json_str.get('count')
            print("Number of results: {}".format(results))
            for result in json_str.get('results'):
                print(result.get('name'))
    except:
        print("Not a valid JSON")
