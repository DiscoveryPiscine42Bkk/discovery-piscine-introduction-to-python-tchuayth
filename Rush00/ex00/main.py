def display_menu():
    print("\n--- Daily Farm Task Manager ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Delete Task")
    print("4. Summarize Tasks by Category")
    print("5. Exit")


def add_task(tasks):
    category = input("Enter task category (watering/spraying/harvesting/animals): ").strip().lower()
    description = input("Enter task description: ").strip()

    while True:
        day = input("Enter day (1–31): ").strip()
        if day.isdigit() and 1 <= int(day) <= 31:
            break
        print("❌ Please enter a valid day (1–31).")

    while True:
        month = input("Enter month (1–12): ").strip()
        if month.isdigit() and 1 <= int(month) <= 12:
            break
        print("❌ Please enter a valid month (1–12).")

    while True:
        year = input("Enter year (e.g. 2025): ").strip()
        if year.isdigit() and len(year) == 4:
            break
        print("❌ Please enter a valid 4-digit year (e.g. 2025).")

    while True:
        time = input("Enter time (HH:MM): ").strip()
        if ":" in time:
            parts = time.split(":")
            if len(parts) == 2 and all(p.isdigit() for p in parts):
                hour, minute = int(parts[0]), int(parts[1])
                if 0 <= hour <= 23 and 0 <= minute <= 59:
                    break
        print("❌ Please enter valid time format (HH:MM, e.g. 14:30).")

    tasks.append({
        'category': category,
        'description': description,
        'day': day.zfill(2),
        'month': month.zfill(2),
        'year': year,
        'time': time
    })

    print("✅ Task added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. [{task['category']}] {task['description']} - "
                  f"{task['day']}/{task['month']}/{task['year']} at {task['time']}")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"🗑️ Deleted: [{removed['category']}] {removed['description']}")
            else:
                print("⚠️ Invalid number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")


def summarize_tasks(tasks):
    summary = {}
    for task in tasks:
        summary[task['category']] = summary.get(task['category'], 0) + 1

    if not summary:
        print("No tasks to summarize.")
    else:
        print("\n--- Task Summary ---")
        for category, count in summary.items():
            print(f"{category.capitalize()}: {count} task(s)")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Select an option (1–5): ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            summarize_tasks(tasks)
        elif choice == '5':
            print("🙏 Thank you for using our service.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
