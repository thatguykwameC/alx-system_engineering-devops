#!/usr/bin/python3
""" Retrieving Data From a REST-API """
import json
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


def JSON_data_formatter(todo_list, usr_name):
    """ Json Data formatter """
    json_dt = []
    for t in todo_list:
        json_dt.append({
            "task": t["title"],
            "completed": t["completed"],
            "username": usr_name
            })
    return (json_dt)


def save_to_fjson(fname, usr_id, json_dt):
    """ Writes a single item to a JSON file"""
    with open(fname, 'w') as fjson:
        json.dump({str(usr_id): json_dt}, fjson)


def main(usr_id):
    """ Function Wrapper """
    usr = fetch_details(usr_id)
    usr_name = usr["username"]

    todo_list = fetch_todo(usr_id)
    json_dt = JSON_data_formatter(todo_list, usr_name)
    save_to_fjson("{}.json".format(usr_id), usr_id, json_dt)


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
