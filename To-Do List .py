import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\nOptions:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    save_tasks(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
