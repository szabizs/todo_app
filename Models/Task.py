import datetime as dt

class Task:

    def __init__(self, task: str, notes: str, start_date: dt.date, due_date: dt.date, reminder_date: dt.date):
        self.task = task
        self.notes = notes
        self.start_date = start_date
        self.due_date = due_date
        self.reminder_date = reminder_date

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, task):
        self.__task = task

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        self.__notes = notes

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        self.__start_date = start_date

    @property
    def due_date(self):
        return self.__due_date

    @due_date.setter
    def due_date(self, due_date):
        self.__due_date = due_date

    @property
    def reminder_date(self):
        return self.__reminder_date

    @reminder_date.setter
    def reminder_date(self, reminder_date):
        self.__reminder_date = reminder_date
