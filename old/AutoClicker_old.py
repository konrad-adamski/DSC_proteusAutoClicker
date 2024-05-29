import time

import pyautogui


class AutoClicker:
    def __init__(self, file_numb):
        self.file_numb = file_numb
        self.is_running = True  # Zustand, der angibt, ob der AutoClicker läuft

        time.sleep(0.5)  # Warten, um Fehler zu vermeiden
        pyautogui.PAUSE = 0.5  # Standardpause zwischen jeden AutoGui-Befehl

        # Positionierung der Auswahl auf die erste Datei
        pyautogui.press('down')  # Drückt die 'down' Taste einmal
        pyautogui.press('up')  # Drückt die 'up' Taste einmal

    def start(self):
        for i in range(1, int(self.file_numb) + 1):
            if self.is_running:
                print(i)
                if i != 1:
                    pyautogui.press('down')

                self.execute()
                time.sleep(3)   # 3 Sekunden
            else:
                print(f"breaking with {i}")
                break
        return True

    def execute(self):
        #pyautogui.press('enter')
        time.sleep(0.1)

    def stop(self):
        self.is_running = False
        print('Stopping AutoClicker...')
