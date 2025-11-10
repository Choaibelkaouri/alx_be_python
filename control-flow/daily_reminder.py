print("=== Daily Reminder ===")

while True:
    # 1) نطلب معلومات المهمة من المستخدم
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # 2) نحدّد جزء الرسالة حسب الأولوية باستخدام match case
    match priority:
        case "high":
            base_message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            base_message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            base_message = f"Note: '{task}' is a low priority task"
        case _:
            base_message = f"Note: '{task}' has an unknown priority"

    # 3) نعدّل الرسالة حسب واش المهمة مرتبطة بالوقت ولا لا
    if time_bound == "yes":
        final_message = base_message + " that requires immediate attention today!"
    else:
        final_message = base_message + ". Consider completing it when you have free time."

    # 4) نطبع التذكير النهائي
    print()
    print(final_message)
    print()

    # 5) نسمحو للمستخدم يقرر واش يكمل ولا يخرج
    again = input("Do you want to enter another task? (yes/no): ").lower()
    if again != "yes":
        print("Good luck with your tasks today! 👋")
        break
