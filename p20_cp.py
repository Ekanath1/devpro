
# import datetime
# import json
# import os
#
# FILE_NAME = "chanting_data.json"
# MALA_TARGET = 108
#
#
# def load_data():
#
#     today = str(datetime.date.today())
#
#     if os.path.exists(FILE_NAME):
#         with open(FILE_NAME, "r") as file:
#             data = json.load(file)
#
#         if data["date"] != today:
#             data["date"] = today
#             data["today_count"] = 0
#
#         return data
#
#     return {
#         "date": today,
#         "today_count": 0,
#         "lifetime_count": 0
#     }
#
#
# def save_data():
#
#     with open(FILE_NAME, "w") as file:
#         json.dump(data, file, indent=4)
#
#
# def start_chanting():
#
#     data["today_count"] += 1
#     data["lifetime_count"] += 1
#
#     save_data()
#
#     current_mala = data["today_count"] % MALA_TARGET
#
#     print("\nChant Count:", current_mala)
#
#     if current_mala == 0:
#         print("Congratulations! One Mala completed.")
#
#
# def view_progress():
#
#     today_count = data["today_count"]
#
#     completed_malas = today_count // MALA_TARGET
#     current_mala = today_count % MALA_TARGET
#
#     percentage = (current_mala / MALA_TARGET) * 100
#
#     print("\n========== CHANTING PROGRESS ==========")
#
#     print("Date:", data["date"])
#
#     print("Current Mala Count:", current_mala)
#
#     print("Completed Malas Today:", completed_malas)
#
#     print("Today's Total Chants:", today_count)
#
#     print("Lifetime Chant Count:", data["lifetime_count"])
#
#     print("Current Mala Progress:", round(percentage, 2), "%")
#
#     print("=======================================")
#
#
# data = load_data()
#
# print("\nWelcome to Chanting Counter")
#
# print("Current Date and Time:", datetime.datetime.now())
#
# while True:
#
#     print("\n1. Start Chanting")
#     print("2. Stop Chanting")
#     print("3. View Progress")
#     print("4. Exit")
#
#     user_input = input("\nPlease enter your choice: ")
#
#     if user_input == '1':
#
#         start_chanting()
#
#     elif user_input == '2':
#
#         print("\nChanting stopped.")
#
#         view_progress()
#
#     elif user_input == '3':
#
#         view_progress()
#
#     elif user_input == '4':
#
#         save_data()
#
#         print("\nThank you for chanting!")
#
#         print("Your progress has been saved.")
#
#         break
#
#     else:
#
#         print("Invalid choice. Please try again.")


import datetime

print(datetime.datetime.now())

chant_sum = 0
day_sum = 0
life_time_sum = 0

while True:

    print("\n1. Start chanting")
    print("2. Stop chanting")
    print("3. View progress")
    print("4. Exit")

    user_input = input("Please enter your choice: ")

    if user_input == '1':

        chant_sum += 1
        life_time_sum += 1

        print("Chant Count:", chant_sum)

        if chant_sum == 108:
            day_sum += 1
            print("Congratulations! One Mala completed.")

            chant_sum = 0

    elif user_input == '2':

        print("Chanting stopped.")
        print("Current Mala Count:", chant_sum)

    elif user_input == '3':

        print("\n----- Chanting Progress -----")
        print("Current Mala Count:", chant_sum)
        print("Completed Malas Today:", day_sum)
        print("Lifetime Chant Count:", life_time_sum)

    elif user_input == '4':
        print("Thank you for chanting!")
        break

    else:
        print("Enter a valid choice.")
