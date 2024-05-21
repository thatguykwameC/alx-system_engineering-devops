#!/usr/bin/python3
""" Retrieving Data From a REST-API """
import json
import requests

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_details():
    """ Fetches employee details """
    usr_url = "{}/users/".format(API_URL)
    return (requests.get(usr_url).json())


def fetch_todo():
    """ Fetches a TODO-list """
    todo_url = "{}/todos".format(API_URL)
    return (requests.get(todo_url).json())


def items_formatter(todo, usr_name):
    """ Item formatter """
    return ({
            "username": usr_name,
            "task": todo["title"],
            "completed": todo["completed"]
            })


def todos_manager(usrs, todo_list):
    """ Manages/Organizes todo-list by user """
    org_data = {}

    for u in usrs:
        user_id = u["id"]
        usr_name = u["username"]
        org_data[user_id] = []

        for t in todo_list:
            if t["userId"] == user_id:
                org_data[user_id].append(items_formatter(t, usr_name))

    return (org_data)


def JSON_data_formatter(dt):
    """ Json Data formatter """
    return (json.dumps(dt, indent=2))


def save_to_fjson(fname, json_dt):
    """ Writes a single item to a JSON file"""
    JSON_formatted_data = JSON_data_formatter(json_dt)
    with open(fname, 'w') as fjson:
        fjson.write(JSON_formatted_data)


def main():
    """ Function Wrapper """
    usrs = fetch_details()
    todo_list = fetch_todo()
    json_dt = todos_manager(usrs, todo_list)
    save_to_fjson("todo_all_employees.json", json_dt)


if (__name__ == "__main__"):
    """ Runs main function wrapper """
    main()
