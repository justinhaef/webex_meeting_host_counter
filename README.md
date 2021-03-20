# Python Webex Host Counter

## Purpose

This appliation simply uses the Cisco Webex Meetings REST API to gather all the meetings from the current month.  It then counts all the meetings that happened for each host email address.  Concluding in printing out the value of the host email address and the number of meetings they were a host of for that month. 

## How to run

*Python version 3.8.2
1. git clone
2. `pip install -r requirements.txt`
3. Change the value in `.env` file of `ACCESS_TOKEN=` to your access token. 
4. Run `python app.py`

## Caveat

This application is designed to be run only once, at the end of the month.  If this is run multiple times or the user is attempting to gather meetings from a previous month, the code in `app.py` lines `37` and `39` will need to be modified. 