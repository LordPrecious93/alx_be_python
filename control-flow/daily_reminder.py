# daily_reminder.py

# Prompt the user for a task, priority, and time-bound status
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on its priority and time sensitivity
if priority == "high":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    else:
        print(f"Reminder: '{task}' is a high priority task. You should complete it soon.")
elif priority == "medium":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a medium priority task that requires attention today!")
    else:
        print(f"Reminder: '{task}' is a medium priority task. Consider completing it soon.")
elif priority == "low":
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a low priority task. Although not urgent, try to complete it today.")
    else:
        print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
else:
    print("Invalid priority. Please enter high, medium, or low.")

