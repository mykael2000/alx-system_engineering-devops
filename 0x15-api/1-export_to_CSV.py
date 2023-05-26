#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    admin = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/"
    user = requests.get(link + "users/{}".format(admin)).json()
    username = user.get("username")
    tasks = requests.get(link + "todos", params={"userId": admin}).json()

    with open("{}.csv".format(admin), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [admin, username, t.get("completed"), t.get("title")]
            ) for t in tasks]
