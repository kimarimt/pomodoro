from time import sleep
from tkinter import *
from PIL import ImageTk, Image


class App(Tk):
    screen_width = 500
    screen_height = 500
    font = ('Helvetica bold', 48)
    timer_font = ('Helvetica Bold', 32)
    checkmark_font = ('Helvetica Bold', 24)
    green = '#BCE1BE'
    red = '#D0AAA5'
    background_color = '#F8F7E0'
    timer_background_color = '#f16749'

    def __init__(self):
        super().__init__()
        self.checkmarks = []
        self.stop_timer = False
        self.title('Pomodoro')
        self.geometry(f'{self.screen_width}x{self.screen_height}')
        self.resizable(False, False)

        # Canvas
        self.canvas = Canvas(master=self)
        self.canvas.config(
            background=self.background_color,
            width=self.screen_width,
            height=self.screen_height)
        self.canvas.pack()

        # Timer Variables
        self.minute = StringVar(master=self.canvas, value='00')
        self.second = StringVar(master=self.canvas, value='00')

        # Timer Label
        self.label = Label(master=self.canvas)
        self.label.config(
            background=self.background_color,
            foreground=self.green,
            font=self.font,
            text='Timer')
        self.label.place(x=190, y=70)

        # Tomato Img
        img = ImageTk.PhotoImage(Image.open('tomato.png'))
        img_label = Label(master=self.canvas)
        img_label.image = img
        img_label.configure(image=img, background=self.background_color)
        img_label.place(x=155, y=140)

        # Minute Label
        self.minute_label = Label(master=self.canvas)
        self.minute_label.configure(
            textvariable=self.minute,
            font=self.timer_font,
            background=self.timer_background_color)
        self.minute_label.place(x=218, y=250)

        # Colon Label
        colon = Label(master=self.canvas)
        colon.configure(
            text=":",
            font=self.timer_font,
            background=self.timer_background_color)
        colon.place(x=255, y=247)

        # Second Label
        self.second_label = Label(master=self.canvas)
        self.second_label.configure(
            textvariable=self.second,
            font=self.timer_font,
            background=self.timer_background_color)
        self.second_label.place(x=270, y=250)

        # Start Button
        self.start_button = Button(master=self.canvas)
        self.start_button.configure(
            text='START',
            highlightbackground=self.background_color,
            command=self.start_timer)
        self.start_button.place(x=80, y=375)

        # Reset Button
        self.reset_button = Button(master=self.canvas)
        self.reset_button.configure(
            text='RESET',
            highlightbackground=self.background_color,
            command=self.reset_timer)
        self.reset_button.place(x=350, y=375)

    def add_checkmark(self, canvas: Canvas):
        checkmark = Label(master=canvas)
        checkmark.configure(text='✓', foreground=self.green, bg=self.background_color, font=self.checkmark_font)
        self.checkmarks.append(checkmark)

    def display_checkmarks(self):
        x_pos = 215
        
        for checkmark in self.checkmarks:
            checkmark.place(x=x_pos, y=400)
            x_pos += 20

    def start_timer(self):
        self.stop_timer = False
        cycles = 7

        for i in range(cycles, 0, -1):
            if self.stop_timer:
                break

            if i % 2 != 0:
                self.label.config(text='Timer', foreground=self.green)
                self.countdown(minute=25)
            else:
                self.label.config(text='Break', foreground=self.red)
                self.countdown(minute=5)
                self.add_checkmark(self.canvas,)
                self.display_checkmarks()

        if not self.stop_timer:
            self.label.config(text='Long Break', foreground=self.red)
            self.label.place(x=125)
            self.countdown(minute=15)
            self.add_checkmark(self.canvas)
            self.display_checkmarks()
                

    def countdown(self, minute):
        mins = minute
        secs = 59

        for i in range(mins, -1, -1):
            if self.stop_timer:
                break 

            sleep(0.01)
            if i < 10:
                self.minute.set(f'0{i}')
            else:
                self.minute.set(f'{i}')
            self.update()

            for j in range(secs, -1, -1):
                if self.stop_timer:
                    break

                self.second.set(f'{j}')
                sleep(0.01)
                if j < 10:
                    self.second.set(f'0{j}')
                else:
                    self.second.set(f'{j}')
                self.update()
            

    def reset_timer(self):
        self.stop_timer = True
        self.minute.set('00')
        self.second.set('00')
        for checkmark in self.checkmarks:
            checkmark.destroy()
        self.checkmarks.clear()
        self.label.config(text='Timer', foreground=self.green)
        self.label.place(x=190)

