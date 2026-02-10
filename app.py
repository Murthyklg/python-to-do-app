#!/usr/bin/env python3
"""
Simple CLI To-Do List App
Tasks are stored locally in a JSON file.
"""

import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task cannot be empty.")
        return

    task = {
        "title": title,
        "done": False,
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")


def complete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Complete which task number? ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Delete which task number? ")) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    actions = {
        "1": add_task,
        "2": list_tasks,
        "3": complete_task,
        "4": delete_task,
        "5": lambda _: exit(0),
    }

    while True:
        print("\n--- TO-DO APP ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Choose an option: ").strip()
        action = actions.get(choice)

        if action:
            action(tasks)
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()
