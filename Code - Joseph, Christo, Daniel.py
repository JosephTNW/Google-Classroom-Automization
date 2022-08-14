from pynput.mouse import Button, Controller
import time

mouse = Controller()


def cycle1():
    # Join the Meeting (Google Classroom Page)
    time.sleep(8)
    mouse.position = (378, 495)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # Join the Meeting (Google Meets Page)
    mouse.position = (1084, 450)
    time.sleep(10)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # Reload Button
    mouse.position = (92, 49)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # Reload Confirmation
    mouse.position = (882, 163)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)


def cycle2():
    # Join the Meeting (Google Classroom Page)
    time.sleep(8)
    mouse.position = (378, 495)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # Join the Meeting (Google Meets Page)
    mouse.position = (1084, 450)
    time.sleep(10)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # Undo After Clicking on Assignment Page
    mouse.position = (27, 45)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    # Reload Button
    mouse.position = (92, 49)
    time.sleep(1)
    mouse.press(Button.left)
    mouse.release(Button.left)


def minimize():
    # Minimize IDE
    mouse.position = (1472, 0)
    mouse.press(Button.left)
    mouse.release(Button.left)


def last_attempt():
    # Join the Meeting (Last Attempt)
    mouse.position = (1084, 450)
    time.sleep(10)
    mouse.press(Button.left)
    mouse.release(Button.left)


print("Hello! Welcome back to school!")
workTime = float(input("How long would you like to wait your teacher to open a meeting (minutes)?"))
loop = (workTime * 60) / 20
Type = (input("Is the class open sharing with the class?")).lower()
x = 0

if Type == "y":
    minimize()
    while x < loop:
        cycle2()
        x += 1
    last_attempt()
    print("Program has tried " + str(round(loop)) + " times in " + str(workTime * 60 + 10) + " seconds.")
elif Type == "n":
    minimize()
    while x < loop:
        cycle1()
        x += 1
    last_attempt()
    print("Program has tried " + str(round(loop)) + " times in " + str(workTime * 60 + 10) + " seconds.")
else:
    print('Error in receiving open sharing with class')
