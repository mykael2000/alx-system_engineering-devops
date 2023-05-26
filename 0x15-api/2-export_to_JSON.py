#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    admin = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + "users/{}".format(admin)).json()
    username = user.get("username")
    tasks = requests.get(link + "todos", params={"userId": admin}).json()

    with open("{}.json".format(admin), "w") as jsonfile:
        json.dump({admin: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in tasks]}, jsonfile)
