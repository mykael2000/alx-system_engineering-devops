#!/usr/bin/python3
""" Gets a list of data from an api call"""
import requests
import sys

if __name__ == "__main__":
    link = "https://jsonplaceholder.typicode.com/"
    people = requests.get(link + "users/{}".format(sys.argv[1])).json()
    tasks = requests.get(link + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in tasks if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        people.get("name"), len(completed), len(tasks)))
    [print("\t {}".format(c)) for c in completed]
