version = 0.1 
# ©️ Fairet
# ensure_ascii=False

import json
import customtkinter as ctk
import tkinter as tk
import datetime

from config import *
from tasks import *
from logic import *

def main():
    data = loads_from_json()
    show_tasks(data)

    new_task = input("Введите новую задачу или нажмите Enter, чтобы пропустить: ")
    if new_task.strip():
        created_by = input("Введите имя автора задачи: ")
        deadline = input("Введите дедлайн задачи (в формате ГГГГ-ММ-ДД): ")
        # Преобразуем строку с дедлайном в объект datetime.date
        deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()

        # Создаем новую задачу в виде словаря
        new_task_data = {
            "description": new_task,
            "created_by": created_by,
            "created_at": datetime.datetime.now().isoformat(),
            "deadline": deadline_date.isoformat()
        }

        data.append(new_task_data)
        dumps_to_json(data, )
        print("Задача успешно добавлена!")

if __name__ == "__main__":
    main()