import pyttsx3
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")

        self.text = tk.StringVar()
        self.text.set("Enter text here...")

        self.voice = tk.StringVar()
        self.voice.set("male")

        self.speed = tk.StringVar()
        self.speed.set("medium")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.select_tab = ttk.Frame(self.notebook, width=600, height=400)
        self.notebook.add(self.select_tab, text='Select', padding=10)

        self.create_select_tab_widgets()

    def create_select_tab_widgets(self):
        frame = ttk.Frame(self.select_tab, padding="10", style='SkyBlue.TFrame')
        frame.pack(fill='both', expand=True)

        label = ttk.Label(frame, text="Select speed:", style='Header.TLabel')
        label.grid(row=0, column=0, padx=5, pady=5)

        low_button = ttk.Button(frame, text="Low", command=lambda: self.set_speed('low'), style='Speed.TButton')
        low_button.grid(row=1, column=0, padx=5, pady=5, ipadx=10, ipady=5)

        medium_button = ttk.Button(frame, text="Medium", command=lambda: self.set_speed('medium'), style='Speed.TButton')
        medium_button.grid(row=2, column=0, padx=5, pady=5, ipadx=10, ipady=5)

        high_button = ttk.Button(frame, text="High", command=lambda: self.set_speed('high'), style='Speed.TButton')
        high_button.grid(row=3, column=0, padx=5, pady=5, ipadx=10, ipady=5)

    def set_speed(self, speed):
        if speed == 'low':
            self.speed.set(100)
        elif speed == 'medium':
            self.speed.set(200)
        elif speed == 'high':
            self.speed.set(300)

        if hasattr(self, 'speed_tab'):
            self.notebook.forget(self.speed_tab)

        self.speed_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.speed_tab, text=speed.capitalize(), padding=10)

        self.create_speed_tab_widgets()

    def create_speed_tab_widgets(self):
        frame = ttk.Frame(self.speed_tab, padding="10", style='SkyBlue.TFrame')
        frame.pack(fill='both', expand=True)

        label = ttk.Label(frame, text=f"Speed: {self.speed.get()}", style='Header.TLabel')
        label.grid(row=0, column=0, padx=5, pady=5)

        label = ttk.Label(frame, text="Enter text to convert to speech:", style='Header.TLabel')
        label.grid(row=1, column=0, padx=5, pady=5)

        entry = tk.Text(frame, wrap="word", width=50, height=10)
        entry.grid(row=2, column=0, padx=5, pady=5)
        self.text_entry = entry

        male_radio = ttk.Radiobutton(frame, text="Male", variable=self.voice, value="male", style='Radio.TRadiobutton')
        male_radio.grid(row=3, column=0, padx=5, pady=5)

        female_radio = ttk.Radiobutton(frame, text="Female", variable=self.voice, value="female", style='Radio.TRadiobutton')
        female_radio.grid(row=4, column=0, padx=5, pady=5)

        convert_button = ttk.Button(frame, text="Convert", command=self.convert_text, style='Green.TButton')
        convert_button.grid(row=5, column=0, padx=5, pady=5, ipadx=10, ipady=5)
        convert_button.bind('<Enter>', lambda e: convert_button.config(style='Hover.Green.TButton'))
        convert_button.bind('<Leave>', lambda e: convert_button.config(style='Green.TButton'))

        save_button = ttk.Button(frame, text="Save Audio", command=self.save_audio, style='Green.TButton')
        save_button.grid(row=6, column=0, padx=5, pady=5, ipadx=10, ipady=5)
        save_button.bind('<Enter>', lambda e: save_button.config(style='Hover.Green.TButton'))
        save_button.bind('<Leave>', lambda e: save_button.config(style='Green.TButton'))

    def convert_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        voice = self.voice.get()
        speed = float(self.speed.get())
        if text:
            engine = pyttsx3.init()
            if voice == "female":
                engine.setProperty('voice', engine.getProperty('voices')[1].id)
            else:
                engine.setProperty('voice', engine.getProperty('voices')[0].id)
            engine.setProperty('rate', speed)
            engine.say(text)
            engine.runAndWait()

    def save_audio(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        if not text:
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            engine = pyttsx3.init()
            voice = self.voice.get()
            speed = float(self.speed.get())
            if voice == "female":
                engine.setProperty('voice', engine.getProperty('voices')[1].id)
            else:
                engine.setProperty('voice', engine.getProperty('voices')[0].id)
            engine.setProperty('rate', speed)
            engine.save_to_file(text, file_path)
            engine.runAndWait()

def main():
    root = tk.Tk()

    style = ttk.Style()
    style.configure('SkyBlue.TFrame', background='sky blue')
    style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
    style.configure('Green.TButton', foreground='white', background='green', font=('Helvetica', 10, 'bold'), padding=(20, 10))
    style.map('Green.TButton',
              foreground=[('active', 'black')],
              background=[('active', '#aaffaa')])
    style.configure('Hover.Green.TButton', foreground='white', background='dark green', font=('Helvetica', 10, 'bold'), padding=(20, 10))
    style.configure('Speed.TButton', foreground='white', background='blue', font=('Helvetica', 10, 'bold'), padding=(20, 10))
    style.map('Speed.TButton',
              foreground=[('active', 'black')],
              background=[('active', '#aaaaff')])
    style.configure('Hover.Speed.TButton', foreground='white', background='dark blue', font=('Helvetica', 10, 'bold'), padding=(20, 10))

    app = TextToSpeechApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
