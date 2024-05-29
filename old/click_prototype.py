import pyautogui
import time

# Ermittelt die Bildschirmgröße
screen_size = pyautogui.size()

# Zeigt die Bildschirmgröße an
print("Bildschirmgröße:", screen_size)
screen_width, screen_height = screen_size

# Close Button Region
screen_width_80 = int(screen_width * 0.8)
screen_height_20 = int(screen_height * 0.2)
search_region_close = (screen_width_80, 0, screen_width, screen_height_20)


def get_image_location(this_image_path, this_region=None):
    this_location = pyautogui.locateOnScreen(this_image_path, confidence=0.82, region=this_region)

    if this_location:
        this_location_tuple = (this_location.left, this_location.top,
                               this_location.width, this_location.height)
        return pyautogui.center(this_location_tuple)
    else:
        return [0, 0]


# Standardverzögerung von 0,14 Sekunden
pyautogui.PAUSE = 0.14

# init -----------------------------------------
time.sleep(3)

# Drückt die 'down' Taste einmal
pyautogui.press('down')

# Drückt die 'up' Taste einmal
pyautogui.press('up')

# start ----------------------------------------

# Drückt die 'up' Taste einmal
pyautogui.press('enter')
time.sleep(6)
print("continue")
pyautogui.press('enter')
pyautogui.press('enter')

# x-Achse Ändern auf Temperatur
image_path = '../images/button1_x_achse.png'
x, y = get_image_location(image_path)
pyautogui.moveTo(x, y)
pyautogui.click()
pyautogui.press('enter')
time.sleep(0.5)

# eine Kurve anklicken
image_path = '../images/button2_selection.png'
x, y = get_image_location(image_path)
pyautogui.moveTo(x, y)
pyautogui.click()

image_path = '../images/item1_DSC.png'
x, y = get_image_location(image_path)
x += 30
y += 30
pyautogui.moveTo(x, y)
pyautogui.click()


# Klick Extras
image_path = '../images/button4_extras.png'
x, y = get_image_location(image_path)
pyautogui.moveTo(x, y)
pyautogui.click()

# Klick 'Export Data'
pyautogui.PAUSE = 0.02
for _ in range(5):
    pyautogui.press('down')
pyautogui.PAUSE = 0.14
pyautogui.press('enter')


# Klick All
image_path = '../images/button5_all.png'
x, y = get_image_location(image_path)
pyautogui.moveTo(x, y)
pyautogui.click()

# Klick Full Range
image_path = '../images/button6_full_range.png'
x, y = get_image_location(image_path)
pyautogui.moveTo(x, y)
pyautogui.click()

# Export
pyautogui.press('enter')
time.sleep(0.2)
pyautogui.press('enter')
time.sleep(0.2)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
time.sleep(2)

# Close Proteus Thermal Analysis
image_path = '../images/button7_close_proteus.png'
x, y = get_image_location(image_path)
y -= 4
pyautogui.moveTo(x, y)
pyautogui.click()
time.sleep(0.2)
pyautogui.press('down')
pyautogui.press('enter')


