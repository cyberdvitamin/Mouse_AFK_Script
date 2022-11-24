import pyautogui, keyboard, numpy, time

# Getting screen size

ScreenX, ScreenY = pyautogui.size()

# Getting emergency key

print("Please select a key for emergency quitting the loop!")
key = keyboard.read_key()
print("You have selected \'" + key + "\' as an emergency key!")

# Getting current time

now = time.localtime(time.time())

# User interface with time and date

print("Current time: " + str(now.tm_hour) + ":" + str(now.tm_min))
print(str(now.tm_mday) + "." + str(now.tm_mon) + "." + str(now.tm_year))
print("For how long do you want to run this script?")

# Time input from user

time_min = now.tm_min + int(input("How many minutes?\n"))
time_hour = now.tm_hour + int(input("How many hours?\n"))

# Time..

time_day = now.tm_mday
time_mon = now.tm_mon
time_year = now.tm_year

# Minutes debug

if time_min >= 60:
    time_hour += int(time_min / 60)
    time_min = int(time_min % 60)

# Hour debug

if time_hour >= 24:
    time_day += int(time_hour / 23)
    time_hour = int(time_hour % 24)

# Day debug (not the best)

if time_mon % 2 == 0 and time_day > 31:
    time_mon += int(time_day / 31)
    time_day = int(time_day % 31)
elif time_mon % 2 == 1 and time_day > 30:
    time_mon += int(time_day / 30)
    time_day = int(time_day % 30)

# Month debug (again.. not the best)

if time_mon > 12:
    time_mon = 1
    time_year += 1

# Output for how long will the script run

print("The script will run until " + str(time_hour) + ":" + str(time_min))
print(str(time_day) + "." + str(time_mon) + "." + str(now.tm_year))

# Shut down PC option

answer = input("Do you want to add auto shut down at a specific hour? Y/N\n")
answer_bool = False
if answer == 'Y' or answer == 'y':
    shut_down_hour = int(input("What hour of the day?\n"))
    shut_down_min = int(input("What minute of the hour?\n"))
    answer_bool = True

# Loop for mouse movement and shut down

while True:
    while keyboard.is_pressed(key) is False:
        now = time.localtime(time.time())
        if now.tm_mday >= time_day and now.tm_hour >= time_hour and now.tm_min >= time_min:
            break
        else:
            MoveToX = numpy.random.randint(0, ScreenX)
            MoveToY = numpy.random.randint(0, ScreenY)
            MoveToTime = numpy.random.uniform(0.2, 2)
            pyautogui.moveTo(MoveToX, MoveToY, MoveToTime)
            if answer_bool is True and now.tm_hour == shut_down_hour and now.tm_min == shut_down_min:
                pyautogui.hotkey('win', 'r')
                pyautogui.write("shutdown /s")
                pyautogui.press("enter")
                break
    break
