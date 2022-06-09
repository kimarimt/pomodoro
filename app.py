from time import sleep
from tkinter import *
from PIL import ImageTk, Image


class App(Tk):
    screen_width = 500
    screen_height = 500
    font = ('Helvetica bold', 48)
    timer_label_color = '#BCE1BE'
    break_label_color = '#D0AAA5'
    timer_font = ('Helvetica Bold', 32)
    background_color = '#F8F7E0'
    timer_background_color = '#f16749'

    def __init__(self):
        super().__init__()
        self.checkmarks = []

        self.title('Pomodoro')
        self.geometry(f'{self.screen_width}x{self.screen_height}')
        self.resizable(False, False)

        # Canvas
        canvas = Canvas(master=self)
        canvas.config(
            background=self.background_color,
            width=self.screen_width,
            height=self.screen_height)
        canvas.pack()

        # Timer Variables
        self.minute = StringVar(master=canvas, value='00')
        self.second = StringVar(master=canvas, value='00')

        # Timer Label
        self.label = Label(master=canvas)
        self.label.config(
            background=self.background_color,
            foreground='#BCE1BE',
            font=self.font,
            text='Timer')
        self.label.place(x=190, y=70)

        # Tomato Img
        img = ImageTk.PhotoImage(Image.open('tomato.png'))
        img_label = Label(master=canvas)
        img_label.image = img
        img_label.configure(image=img, background=self.background_color)
        img_label.place(x=155, y=140)

        # Minute Label
        self.minute_label = Label(master=canvas)
        self.minute_label.configure(
            textvariable=self.minute,
            font=self.timer_font,
            background=self.timer_background_color)
        self.minute_label.place(x=218, y=250)

        # Colon Label
        colon = Label(master=canvas)
        colon.configure(
            text=":",
            font=self.timer_font,
            background=self.timer_background_color)
        colon.place(x=255, y=247)

        # Second Label
        self.second_label = Label(master=canvas)
        self.second_label.configure(
            textvariable=self.second,
            font=self.timer_font,
            background=self.timer_background_color)
        self.second_label.place(x=270, y=250)

        # Start Button
        self.start_button = Button(master=canvas)
        self.start_button.configure(
            text='START',
            highlightbackground=self.background_color,
            command=self.start_timer)
        self.start_button.place(x=80, y=375)

        # Reset Button
        self.reset_button = Button(master=canvas)
        self.reset_button.configure(
            text='RESET',
            highlightbackground=self.background_color,
            command=self.reset_timer)
        self.reset_button.place(x=350, y=375)

    def start_timer(self):
        cycles = 7

        for i in range(cycles, 0, -1):
            if i % 2 != 0:
                self.label.config(text='Timer', foreground=self.timer_label_color)
                self.countdown(1)
            else:
                self.label.config(text='Break', foreground=self.break_label_color)
                self.countdown(1)

        self.label.config(text='Long Break', foreground=self.break_label_color)
        self.label.place(x=125)
        self.countdown(1)
                

    def countdown(self, minute):
        minute = minute
        secs = 59

        self.minute.set(f'0{minute}')
        for i in range(minute, -1, -1):
            self.second.set(f'{secs}')
            for i in range(secs, -1, -1):
                sleep(0.01)
                if i < 10:
                    self.second.set(f'0{i}')
                else:
                    self.second.set(f'{i}')
                self.update()
            
            if i != 0:
                secs = 59
                self.second.set(f'{secs}')
            
            sleep(0.01)
            if i < 10:
                self.minute.set(f'0{i}')
            else:
                self.minute.set(f'{i}')
            
            self.update()

    
    def reset_timer(self):
        print('Timer reset')
