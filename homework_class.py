class ToDoList:
    def __init__(self):
        self.task = {}

    def add_task(self, task):
        self.task[len(self.task) + 1] = {}
        self.task[len(self.task)]["Задача"] = task
        self.task[len(self.task)]["Состояние"] = "Не выполнено"

    def remove_task(self, task):
        del self.task[task]
        print("Задача удалена")
        keys = list(self.task.keys())
        for i in range(len(self.task)):  # Переименовываю ключи в правильном порядке
            self.task[i + 1] = self.task.pop(keys[i])

    def list_tasks(self):
        if len(self.task) != 0:
            for key in self.task:
                print(f"{key}: {self.task[key]["Задача"]} | {self.task[key]["Состояние"]}")
        else:
            print("Задач нет")

    def complete_task(self, task):
        self.task[task]["Состояние"] = "Выполнено"
        print("Задача выполнена")


tasks = ToDoList()
menu = {1: {"Название": "Список задач", "Функция": tasks.list_tasks},
        2: {"Название": "Добавить задачу", "Функция": tasks.add_task},
        3: {"Название": "Удалить задачу", "Функция": tasks.remove_task},
        4: {"Название": "Выполнить задачу", "Функция": tasks.complete_task},
        0: {"Название": "Выход"}}
try:
    while True:
        print("")  # Для лучшей читаемости в консоли
        for i in menu:
            print(f"{i} - {menu[i]["Название"]}")
        action = int(input("Выберите действие: "))
        if action == 0:
            break
        elif action == 1:
            menu[action]["Функция"]()
        elif action == 2:
            menu[action]["Функция"](input("Введите задачу: "))
        elif action == 3 or action == 4:
            menu[action]["Функция"](int(input("Введите № задачи: ")))
except ValueError:
    print("Неверный тип данных.")
