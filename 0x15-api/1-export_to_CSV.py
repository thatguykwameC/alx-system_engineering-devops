#!/usr/bin/python3
""" Retrieving Data From a REST-API """
import csv
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_details(usr_id):
    """ Fetches employee details """
    usr_url = "{}/users/{}".format(API_URL, usr_id)
    return (requests.get(usr_url).json())


def fetch_todo(usr_id):
    """ Fetches a TODO-list """
    todo_url = "{}/todos?userId={}".format(API_URL, usr_id)
    return (requests.get(todo_url).json())


def input_to_fcsv(fname, lst, username):
    """ Writes a single item to a CSV file"""
    with open(fname, 'a', newline='') as fcsv:
        csv.writer(fcsv, quoting=csv.QUOTE_ALL).writerow([
                        lst["userId"],
                        username,
                        str(lst["completed"]),
                        lst["title"]
                        ])


def csv_export(todo_list, usr_id, usr_name):
    """ Export list to CSV """
    fname = "{}.csv".format(usr_id)

    with open(fname, 'w', newline='') as fcsv:
        pass

    for t in todo_list:
        input_to_fcsv(fname, t, usr_name)


def main(usr_id):
    """ Function Wrapper """
    usr = fetch_details(usr_id)
    usr_name = usr["username"]

    todo_list = fetch_todo(usr_id)
    csv_export(todo_list, usr_id, usr_name)


if (__name__ == "__main__"):
    """
        Checks if the script is being run correctly as the format suggest
        Format => python3 script_name.py user_id_integer_type
        Checks if the employee_id is an intger type or not
    """
    if len(sys.argv) != 2:
        print("USAGE: python3 script_name.py user_id_integer_type")
        sys.exit(1)

    try:
        usr_id = int(sys.argv[1])
        main(usr_id)
    except ValueError:
        print("User ID must be an integer.")
        sys.exit(1)
