class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = ""

    def update_task(self, task, new_task):
        if task in self.tasks:
            self.tasks[new_task] = self.tasks.pop(task)
        else:
            print("Task not found.")

    def remove_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
        else:
            print("Task not found.")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for task, description in self.tasks.items():
                print(task)
        else:
            print("No tasks in the to-do list.")

if __name__ == "__main__":
    todo_list = ToDoList()
    print("\n ********** WELCOME TO TO-DO LIST ***********")

    while True:
        
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            todo_list.update_task(task, new_task)
            print("Task updated successfully.")
        elif choice == "3":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
            print("Task removed successfully.")
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



