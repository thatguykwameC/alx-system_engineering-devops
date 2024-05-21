#!/usr/bin/python3
""" Retrieving Data From a REST-API """
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def fetch_details(employee_id):
    """ Fetches employee details """
    usr_url = "{}/users/{}".format(API_URL, employee_id)
    return (requests.get(usr_url).json())


def fetch_todo(employee_id):
    """ Fetches a TODO-list """
    todo_url = "{}/todos?userId={}".format(API_URL, employee_id)
    return (requests.get(todo_url).json())


def calc_prog(todos_nums):
    """ Calculates number of done/total tasks (todos progress) """
    total_number_of_tasks = len(todos_nums)
    number_of_done_tasks = len([t for t in todos_nums if t['completed']])
    return (total_number_of_tasks, number_of_done_tasks)


def prog_display(todos, employee_name, number_of_done_tasks,
                 total_number_of_tasks):
    """ Displays todos progress """
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_of_done_tasks, total_number_of_tasks))
    for t in todos:
        if t['completed']:
            print("\t {}".format(t['title']))


def main(employee_id):
    """ Function Wrapper """
    employee = fetch_details(employee_id)
    employee_name = employee['name']

    todo_list = fetch_todo(employee_id)
    (total_number_of_tasks, done_tasks) = calc_prog(todo_list)

    prog_display(todo_list, employee_name, done_tasks, total_number_of_tasks)


if (__name__ == "__main__"):
    """
        Checks if the script is being run correctly as the format suggest
        Format => python3 script_name.py employee_id_integer_type
        Checks if the employee_id is an intger type or not
    """
    if len(sys.argv) != 2:
        print("USAGE: python3 script_name.py employee_id_integer_type")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        main(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
