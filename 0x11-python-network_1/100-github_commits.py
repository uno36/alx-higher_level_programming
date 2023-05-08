#!/usr/bin/python3
"""
 a Python script that takes 2 arguments that list 10 commits (from
the most recent to oldest) of the repository “rails” by the user “rails”
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    r = requests.get(url)
    json = r.json()
    count = 1
    for i in json:
        print(i.get('sha') + ':', i.get('commit').get('author').get('name'))
        if count == 10:
            break
        count += 1
