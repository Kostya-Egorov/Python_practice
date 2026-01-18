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
menu = {1: {"Название": "Список задач", "Функция": lambda x: tasks.list_tasks()},
        2: {"Название": "Добавить задачу", "Функция": lambda x: tasks.add_task(input("Введите задачу: "))},
        3: {"Название": "Удалить задачу", "Функция": lambda x: tasks.remove_task(int(input("Введите № задачи: ")))},
        4: {"Название": "Выполнить задачу", "Функция": lambda x: tasks.complete_task(int(input("Введите № задачи: ")))},
        0: {"Название": "Выход"}}
while True:
    try:
        print("")  # Для лучшей читаемости в консоли
        for i in menu:
            print(f"{i} - {menu[i]["Название"]}")
        action = int(input("Выберите действие: "))
        if action == 0:
            break
        else:
            menu[action]["Функция"](1)
    except ValueError:
        print("Неверный тип данных.")
