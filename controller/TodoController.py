from models import Task

import os
import csv
import time
import datetime
import pandas as pd

PAGE_WIDTH = 100
TASKS_FILE = './data/tasks.csv'
OPTIONS = {
    '1': 'Add task',
    '2': 'Edit task',
    '3': 'Delete task',
    '4': 'List all tasks',
    '5': 'Exit (Ctrl + c)'
}

HEADER = ['Task', 'Notes', 'Start date', 'Due date', 'Remind date']


class Todo:

    accepted_values = [1, 2, 3, 4, 5]
    user_action = ''

    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def todo_logger(self):
        return self.__todo_logger

    @todo_logger.setter
    def todo_logger(self, todo_logger):
        self.__todo_logger = todo_logger

    @property
    def app_title(self):
        return self.__app_title

    @app_title.setter
    def app_title(self, app_title):
        self.__app_title = app_title

    @property
    def page_width(self):
        return int(self.__page_width)

    @page_width.setter
    def page_width(self, page_width = 130):
        self.__page_width = page_width

    @page_width.getter
    def page_width(self):
        return self.__page_width

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks):
        self.__tasks = tasks

    @property
    def total_tasks(self):
        return self.__total_tasks

    @total_tasks.setter
    def total_tasks(self, total_tasks):
        self.__total_tasks = total_tasks

    # def __init__(self):
    #     self.ld_tsk_to_mem(self)
    #     self.clear()
    #     self.init_interface()
    #     self.get_input()

    @staticmethod
    def clear():
        os.system('cls')

    def init_interface(self):
        self.todo_logger.debug('Loading interface.')
        print(self.bordered(self.app_title))
        print('┌' + ''.center(self.page_width, '─') + '┐')
        for key, value in OPTIONS.items():
            print('│' + (' ' * 30) + key + '.' + value.ljust(self.page_width - 32, ' ') + '│')
        print('└' + (' Total tasks: ' + str(self.total_tasks) + ' ').center(self.page_width, '─') + '┘')
        self.todo_logger.debug('Interface has loaded.')

    @staticmethod
    def total_tasks(self):
        return str(len(self.tasks))

    def ld_tsk_to_mem(self):
        self.todo_logger.debug('Start loading tasks into memory.')
        df = pd.read_csv(TASKS_FILE, names=HEADER)
        self.tasks = df.to_dict('index')
        self.total_tasks = len(self.tasks)
        self.todo_logger.debug('Loaded a total of ' + str(self.total_tasks) + ' tasks into memory.')

    def get_input(self):
        self.todo_logger.debug('Waiting for input from user.')
        self.user_action = int(input('Chose an action: '))
        self.todo_logger.debug(f'Got input [{self.user_action}] from user.')
        if self.user_action in self.accepted_values:
            if self.user_action == 1:
                self.add_new_task()
            elif self.user_action == 4:
                self.list_all_tasks()
            elif self.user_action == 3:
                self.delete_task()
            elif self.user_action == 5:
                self.exit_app()
            elif self.user_action == 2:
                self.edit_task()
        else:
            self.clear()
            self.init_interface()
            self.re_initialize(input('Value not accepted, select between (1 an 5). \nNew choice: '))

    def edit_task(self):
        self.clear()
        self.list_all_tasks()
        print(self.bordered('Editing tasks', PAGE_WIDTH))
        row_index = int(input('Enter task ID to edit: ')) - 1
        df = pd.read_csv(TASKS_FILE, header=None)

        task_name = input('Task name [' + df[0][row_index] + ']: ')
        task_name = task_name or df[0][row_index]

        task_notes = input('Task notes [' + df[1][row_index] + ']: ')
        task_notes = task_notes or df[1][row_index]

        start_date = input('Start date (yyyy-mm-dd) [' + df[2][row_index] + ']: ')
        start_date = start_date or df[2][row_index]

        due_date = input('Due date (yyyy-mm-dd) [' + df[3][row_index] + ']: ')
        due_date = due_date or df[3][row_index]

        reminder_date = input('Reminder date (yyyy-mm-dd) [' + df[4][row_index] + ']: ')
        reminder_date = reminder_date or df[4][row_index]

        df[0][row_index] = task_name
        df[1][row_index] = task_notes
        df[2][row_index] = start_date
        df[3][row_index] = due_date
        df[4][row_index] = reminder_date

        df.to_csv(TASKS_FILE, index=False, header=False)
        print(self.bordered('Your task has been edited! Clearing screen, taking you back to home.'.center(PAGE_WIDTH, ' '), PAGE_WIDTH))

        count_down = 3
        self.countdown_timer(count_down)
        self.__init__()

    def delete_task(self):
        self.clear()
        self.list_all_tasks()
        print(self.bordered('Deleting tasks', PAGE_WIDTH))

        row_index = int(input('Enter task ID to delete the task: ')) - 1

        df = pd.read_csv(TASKS_FILE, header=None)
        df.drop(df.index[[row_index, ]], inplace=True)
        df.to_csv(TASKS_FILE, index=False, header=False)

        print(self.bordered('Your task has been deleted! Clearing screen, taking you back to home.'.center(PAGE_WIDTH, ' '), PAGE_WIDTH))
        count_down = 3
        self.countdown_timer(count_down)
        self.__init__()

    def add_new_task(self):
        self.clear()
        self.init_interface()

        print(self.bordered('Add new task'.center(PAGE_WIDTH, ' '), PAGE_WIDTH))

        task_name = input('Task name: ')
        task_notes = input('Task notes: ')
        start_date = input('Start date (yyyy-mm-dd): ')
        due_date = input('Due date (yyyy-mm-dd): ')
        reminder_date = input('Reminder date (yyyy-mm-dd): ')

        task = Task(task_name, task_notes, start_date, due_date, reminder_date)
        print(task.task)


        row = [task_name, task_notes, start_date, due_date, reminder_date]

        with open(TASKS_FILE, 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

        print(self.bordered('Your task has been saved! Clearing screen, taking you back to home.'.center(PAGE_WIDTH, ' '), PAGE_WIDTH))
        count_down = 3
        self.countdown_timer(count_down)
        self.__init__()

    def list_all_tasks(self):
        self.todo_logger.debug('Clearing screen.')
        self.clear()

        csv_header = (cell.ljust(30, ' ') for cell in HEADER)
        print('Id'.ljust(5, ' '), *csv_header)
        print(''.center(150, '─'))
        self.todo_logger.debug(f'Displaying [{len(self.tasks)}] tasks into view.')
        for index in self.tasks:
            print(str(index+1).ljust(5, ' '), *(self.tasks[index][data].ljust(30, ' ') for data in self.tasks[index]))

    def exit_app(self):
        print(self.bordered('See you soon. App will exit now...'))
        self.countdown_timer(3)
        self.running = False
        self.todo_logger.debug('Exiting app, setting running to False.')
        self.clear()

    def re_initialize(self, replay):
        if replay in self.accepted_values:
            self.clear()
        else:
            self.re_initialize(input('Value not accepted! Try again? (y/n) \nYour choice: '))

    def countdown_timer(self, x):
        while x > 0:
            x -= 1
            print("{} remaining".format(str(datetime.timedelta(seconds=x))))
            time.sleep(1)

    def bordered(self, text):
        lines = text.splitlines()
        width = self.page_width
        res = ['┌' + '─' * width + '┐']
        for s in lines:
            res.append('│' + (s + ' ' * width)[:width] + '│')
        res.append('└' + '─' * width + '┘')
        return '\n'.join(res)

    @staticmethod
    def get_csv_lines():
        return sum(1 for row in TASKS_FILE)
