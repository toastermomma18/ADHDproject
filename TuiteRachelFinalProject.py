"""
    This is my final project for SDEV 140. This is a basic app to help ADHD kids to remember their routines and help parents. ADHD is something that my daughter and husband struggle
    with. This app will help them keep track of routines, important dates and tasks that need to be completed every day. This app is called Focus Finder.
"""


import tkinter as tk #tkinter is the GUI platform I used to create the app. 
import datetime


class Task:
    def __init__(self, title, due_date, routine):
        self.title = title
        self.due_date = due_date
        self.routine = routine
        self.completed = False

class FocusFinderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Focus Finder App")

        

        # Create a button to open the settings window
        self.settings_button = tk.Button(self.root, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=8, column=0, columnspan=4)

    def open_settings(self):
        settings_window = SettingsWindow(self)
        settings_window.grab_set()  # Make the child window modal
        settings_window.wait_window()  # Wait for the child window to close


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.geometry("300x200")

        # Add your settings options here
        label = tk.Label(self, text="Settings")
        label.pack(pady=10)

        # Create buttons or other widgets for settings

if __name__ == "__main__":
    app = FocusFinderApp()




class Task:
    def __init__(self, title, due_date, routine):
        self.title = title
        self.due_date = due_date
        self.routine = routine
        self.completed = False

class FocusFinderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Focus Finder App")

        # ... (rest of your code)

        # Create a button to open the settings window
        self.settings_button = tk.Button(self.root, text="Settings", command=self.open_settings)
        self.settings_button.grid(row=8, column=0, columnspan=4)

    def open_settings(self):
        settings_window = SettingsWindow(self)
        settings_window.grab_set()  # Make the child window modal
        settings_window.wait_window()  # Wait for the child window to close






class Task:
    def __init__(self, title, due_date, routine):
        self.title = title
        self.due_date = due_date
        self.routine = routine
        self.completed = False

class FocusFinderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Focus Finder App")

        # Create widgets
        self.task_entry = tk.Entry(self.root)
        self.due_date_entry = tk.Entry(self.root)
        self.routine_entry = tk.Entry(self.root)
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.task_list = tk.Listbox(self.root)

        self.calendar_label = tk.Label(self.root, text="")
        self.routine_label = tk.Label(self.root, text="")

        # Pack widgets
        self.task_entry.grid(row=0, column=0)
        self.due_date_entry.grid(row=0, column=1)
        self.routine_entry.grid(row=0, column=2)
        self.add_button.grid(row=0, column=3)
        self.task_list.grid(row=1, column=0, rowspan=5, columnspan=4)
        self.calendar_label.grid(row=6, column=0, columnspan=4)
        self.routine_label.grid(row=7, column=0, columnspan=4)

        # Initialize variables
        self.tasks = []
        self.update_calendar()
        self.update_routine()

        self.root.mainloop()

    def add_task(self):
        title = self.task_entry.get()
        due_date = self.due_date_entry.get()
        routine = self.routine_entry.get()
        task = Task(title, due_date, routine)
        self.tasks.append(task)
        self.update_task_list()
        self.update_calendar()
        self.update_routine()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, f"{task.title} ({task.due_date})")

    def update_calendar(self):
        today = datetime.date.today()
        calendar_text = f"Today: {today.strftime('%A, %B %d, %Y')}"
        self.calendar_label.config(text=calendar_text)

    def update_routine(self):
        routine_text = "Your Daily Routine:\n"
        for task in self.tasks:
            if task.routine:
                routine_text += f"  - {task.title}\n"
        self.routine_label.config(text=routine_text)

if __name__ == "__main__":
    app = FocusFinderApp()
    