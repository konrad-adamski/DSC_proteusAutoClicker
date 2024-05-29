import time

import pyautogui


class AutoClicker:
    def __init__(self, file_numb, delay_factor=1.0, demo=False):
        self.delay = file_numb  # TODO
        self.is_running = True  # Zustand, der angibt, ob der AutoClicker läuft

        self.delay_factor = delay_factor
        self.demo = demo
        self.demo = True

        if self.demo:
            pyautogui.PAUSE = 1.2 * self.delay_factor  # Standardpause zwischen jeden AutoGui-Befehl
            self.sleep = 1 * self.delay_factor
        else:
            pyautogui.PAUSE = 0.4 * self.delay_factor
            self.sleep = 0.5 * delay_factor
            print("kein Demo")

        time.sleep(self.sleep)  # Warten, um Fehler zu vermeiden

    def start(self):
        # Auswahl aller Dateien im Ordner
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(self.sleep)
        print("Dateien ausgewählt")

        # Start von Proteus
        pyautogui.press('enter')
        time.sleep(8)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(self.sleep)
        print("Protheus wurde erfolgreich gestartet")

        # x-Achse Ändern auf Temperatur
        self.change_x_axis()
        print("x-Ache verändert")

        # eine Kurve auswählen
        self.select_curve()
        print("Kurve ausgewählt")

        # Extras und 'Export Data'
        self.extras_export()
        self.export_settings()
        self.export_text()

        # Proteus Software Schließen
        self.close_proteus()

    def change_x_axis(self):
        image_path = 'images/button1_x_achse.png'
        x, y = get_image_location(image_path)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.press('enter')
        time.sleep(2 * self.sleep)

    def select_curve(self):
        image_path = 'images/button2_selection.png'
        x, y = get_image_location(image_path)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(1 + self.sleep)

        image_path = 'images/item1_DSC.png'
        dsc_x, dsc_y = get_image_location(image_path)
        time.sleep(1 + self.sleep)

        x = dsc_x + 30
        y = dsc_y + 30
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(1 + self.sleep)

    def extras_export(self):
        # Klick Extras
        image_path = 'images/button4_extras.png'
        x, y = get_image_location(image_path)
        pyautogui.moveTo(x, y)
        pyautogui.click()

        # Klick 'Export Data'
        if self.demo is False:
            pyautogui.PAUSE /= 2
            print("kein Demo")

        for _ in range(5):
            pyautogui.press('down')
        if self.demo is False:
            pyautogui.PAUSE *= 2

        pyautogui.press('enter')
        time.sleep(self.sleep)

    def export_settings(self):
        # Klick All
        time.sleep(1)
        image_path = 'images/button5_all.png'
        x, y = get_image_location(image_path)
        pyautogui.moveTo(x, y)
        pyautogui.click()

        # Klick Full Range
        image_path = 'images/button6_full_range.png'
        x, y = get_image_location(image_path)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(self.sleep)

    def export_text(self):
        pyautogui.press('enter')
        time.sleep(0.2 * self.sleep)
        if self.demo:
            time.sleep(self.sleep)
        pyautogui.press('enter')
        time.sleep(0.2 * self.sleep)

        try:
            image_path = 'images/info_image.png'
            get_image_location(image_path)
            pyautogui.press('enter')
            time.sleep(self.sleep)
        except pyautogui.ImageNotFoundException:
            print("Keine Info")

        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(0.2 * self.sleep)

    def close_proteus(self):
        image_path = 'images/button7_close_proteus.png'
        x, y = get_image_location(image_path)
        y -= 4
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2 * self.sleep)
        pyautogui.press('down')
        pyautogui.press('enter')


def get_image_location(this_image_path, this_confidence=0.82):
    this_location = pyautogui.locateOnScreen(this_image_path, confidence=this_confidence)

    if this_location:
        this_location_tuple = (this_location.left, this_location.top,
                               this_location.width, this_location.height)
        return pyautogui.center(this_location_tuple)
    else:
        return [0, 0]


