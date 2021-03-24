# Python Webex Host Counter

## This is not for use in production, this is a demonstration of how to use OAuth and Webex API.  Use at your own discretion. 

## Purpose

This appliation simply uses the Cisco Webex Meetings REST API to gather all the meetings from the current month.  It then counts all the meetings that happened for each host email address.  Concluding in printing out the value of the host email address and the number of meetings they were a host of for that month. 

## How to run

>Only tested on Python version 3.8.2

>This assumes you've already created your [Webex Integrations](https://developer.webex.com/docs/integrations).

> Helpful OAuth2.0 Summary for Webex [Walk Through](https://developer.webex.com/blog/real-world-walkthrough-of-building-an-oauth-webex-integration)
1. `git clone https://github.com/justinhaef/webex_meeting_host_counter.git`
1. `pip install -r requirements.txt`
1. Rename `.env_template` to `.env`.
1. Change the values in `.env` file to your values. 
1. Run `python auth.py` to get the Access and Refresh Tokens
1. Add those values to your `.env` file.
1. Run `python app.py`

## Caveat

This application is designed to be run only once, at the end of the month.  If this is run multiple times or the user is attempting to gather meetings from a previous month, the code in `app.py` line `76` will need to be modified. 
