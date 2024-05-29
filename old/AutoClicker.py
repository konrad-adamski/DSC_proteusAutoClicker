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
        pyautogui.keyDown('shift')
        for _ in range(int(self.file_numb)):
            pyautogui.press('down')
        pyautogui.keyUp('shift')

