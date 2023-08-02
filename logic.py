# ©️ Fairet

import json
import customtkinter as ctk
import tkinter as tk

def show_tasks(data):
    """Show all tasks from tasks.json"""
    print("Todo List:")
    for task in data:
        print(f"- {task['description']}")
        print(f"  Created by: {task['created_by']}")
        print(f"  Created at: {task['created_at']}")
        print(f"  Deadline: {task['deadline']}")
        print()


def dumps_to_json(data):
    """Dump to json file"""
    new_data = json.dumps(data, ensure_ascii=False)
    with open('juniors_and_seniors/tasks.json', 'w') as file:
        json.dump(new_data, file, indent=2)

def loads_from_json():
    """Parse from json"""
    try:
        with open('juniors_and_seniors/tasks.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# def create_tasks(data):
#     """Creating a tasks to json file"""
#     for item in data