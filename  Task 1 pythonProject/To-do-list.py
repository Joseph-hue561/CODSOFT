import os


def add_task(tasks, description, due_date):
    tasks.append({"description": description, "due_date": due_date})
    print("Task Added Successfully ✔")


def view_task(tasks):
    if not tasks:
        print("No Tasks Found.")
    else:
        print("Tasks: ")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['description']} - Due Date: {task['due_date']}")


def delete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task Deleted Successfully ❌")
    else:
        print("Invalid task index.")


def save_task_to_file(tasks, file_path):
    with open(file_path, 'w') as f:
        for task in tasks:
            f.write(f"{task['description']}|{task['due_date']}\n")


def load_task_from_file(file_path):
    tasks = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                if '|' in line:
                    description, due_date = line.strip().split('|')
                    tasks.append({"description": description, "due_date": due_date})
    return tasks


def main():
    tasks = []
    file_path = "tasks.txt"
    tasks = load_task_from_file(file_path)

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task Description: ")
            due_date = input("Enter Due Date: ")
            add_task(tasks, description, due_date)
            save_task_to_file(tasks, file_path)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            view_task(tasks)
            try:
                task_index = int(input("Enter the task index to Delete: "))
                delete_task(tasks, task_index)
                save_task_to_file(tasks, file_path)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
