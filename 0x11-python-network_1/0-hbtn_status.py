#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        utf8_content = content.decode('utf8')
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(content), content, utf8_content))
