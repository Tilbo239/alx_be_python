task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

priorites = ["high", "medium", "low"]

print(priority in priorites)

match priority:
    case "high":
        reminde = f"'{task}' is a {priority} priority task"
    case "medium":
        reminde = f"'{task}' is a {priority} priority task"
    case "low":
        reminde = f"'{task}'  is a {priority} priority task."
if priority in priorites and is_time_bound == "yes":
    print(f"Reminder : {reminde} that require immediate attention today!")

if priority in priorites and is_time_bound == "no":
    print(f"Reminder : {reminde} Consider completing it when you have free time.")
