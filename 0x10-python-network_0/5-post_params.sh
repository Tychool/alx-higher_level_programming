#!/bin/bash
# tis script will send a POST request to the passed URL,
# and display the body of the response

curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
