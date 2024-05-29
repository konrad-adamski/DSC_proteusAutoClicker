import threading
import tkinter as tk
from tkinter import filedialog, messagebox

from AutoClicker import AutoClicker
from utils import file_count
import os


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DSC AutoClicker")
        self.minsize(600, 300)

        self.directory_path = tk.StringVar(self)

        select_button = tk.Button(self, text="Quellverzeichnis wählen", command=self.select_directory)
        select_button.grid(row=0, column=0, padx=(10, 5), pady=(10, 0), sticky="ew")
        select_button.config(width=20)

        self.path_entry = tk.Entry(self, textvariable=self.directory_path, state="readonly")
        self.path_entry.grid(row=0, column=1, padx=(5, 10), pady=(10, 0), sticky="ew")
        self.path_entry.config(width=50)

        self.start_button = tk.Button(self, text="Start", command=self.open_directory, state="disabled")
        self.start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=(10, 10), sticky='w')
        self.start_button.config(width=20)

        self.stop_button = tk.Button(self, text="Stop", command=self.stop_clicker, state="disabled")
        self.stop_button.grid(row=3, column=0, columnspan=2, padx=10, pady=(10, 10), sticky='w')
        self.stop_button.config(width=20)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

    def open_directory(self):
        if self.directory_path.get():
            os.startfile(self.directory_path.get())
            file_numb = file_count(self.directory_path.get())
            self.clicker = AutoClicker(file_numb)
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

            # Starte den AutoClicker in einem separaten Thread
            self.clicker_thread = threading.Thread(target=self.clicker.start)
            self.clicker_thread.start()


        else:
            messagebox.showinfo("Information", "Bitte beide Verzeichnisse auswählen!")

    def stop_clicker(self):
        if hasattr(self, 'clicker') and self.clicker:
            self.clicker.stop()
            self.stop_button.config(state="disabled")
            self.start_button.config(state="normal")
            if hasattr(self, 'clicker_thread') and self.clicker_thread.is_alive():
                self.clicker_thread.join()  # Warten, bis der Thread beendet ist
                del self.clicker_thread  # Lösche den Thread
            del self.clicker  # Lösche die clicker-Instanz


    def select_directory(self):
        dirname = filedialog.askdirectory(parent=self)
        if dirname:
            self.directory_path.set(dirname)
            self.check_paths()

    def select_target_directory(self):
        dirname = filedialog.askdirectory(parent=self)
        if dirname:
            self.check_paths()

    def check_paths(self):
        if self.directory_path.get():
            self.start_button.config(state="normal")
        else:
            self.start_button.config(state="disabled")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
