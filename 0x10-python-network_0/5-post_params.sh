#!/bin/bash
# Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -s "$1"
