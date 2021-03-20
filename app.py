from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()
import os
import requests
import json

access_token = os.getenv("ACCESS_TOKEN")
base_url = 'https://webexapis.com/v1'


def main(from_date: str, to_date: str, meetingType: str='meeting'):
    """ Main entry point for the application.
    """
    url = f'{base_url}/meetings?meetingType={meetingType}&from={from_date}&to={to_date}'
    response = requests.get(url=url, headers={'Authorization': f'Bearer {access_token}'})
    return response


def count_hosts(meetings):
    """ Dedicated fuction to only count
        specific hosts
    """
    # Create an empty dictionary for hosts
    host_dict = dict()
    for item in meetings['items']:
        # Check if the host is already counted
        if item['hostEmail'] not in host_dict.keys():
            host_dict[item['hostEmail']] = 1
        else:
            host_dict[item['hostEmail']] += 1
    return host_dict
        

if __name__ == "__main__":
    # Get today's date
    ending_date= datetime.today().date()
    # Replace the day from today's date to 1 to get the 1st day of month
    starting_date = ending_date.replace(day=1)

    response = main(from_date=starting_date, to_date=ending_date)
    json_response = json.loads(response.text)
    hosts = count_hosts(json_response)
    # For demo only
    print(json.dumps(hosts, indent=4))
