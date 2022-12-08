from tkinter import *
from tkinter import filedialog
from time import *
import pygame

""" Set global alarm time for Null """
set_alarm = ""
""" Set default ringtone """
ringtone = "data/ringtone.mp3"

""" Create TKinter intance of window """
window = Tk()
window.geometry("650x650")
window.title("ALARM CLOCK")
window.config(background="#a79aab")

""" Set icon image """
icon = PhotoImage(file="data/alarm-clock.png")
window.iconphoto(True, icon)


def upload_mp3():
    """Input custom rington"""
    filepath = filedialog.askopenfilename(
        title="Select ringtone for alarm", filetypes=(("mp3 Files", "*.mp3"),)
    )
    global ringtone
    ringtone = filepath


""" Create TKinter Import ringtone button with custom ringtone function """
button_ringtone = Button(
    window,
    text="set ringtone",
    command=upload_mp3,
    font=("Trebuchet", 20, "bold"),
    bg="#a79aab",
    activebackground="#584c5c",
    width=12,
)
button_ringtone.place(x=10, y=300)


def set_alarm_time():
    """Set alarm time fuction from Spinbox input"""
    global set_alarm
    print(f"{scale_hours.get()}:{scale_minutes.get()}:{scale_seconds.get()}")
    # button_submit.config(state=DISABLED)
    set_alarm = f"{scale_hours.get()}:{scale_minutes.get()}:{scale_seconds.get()}"
    return set_alarm


""" Create TKinter set alarm button for submit Spinbox input """
button_submit = Button(
    window,
    text="Set alarm",
    command=set_alarm_time,
    font=("Trebuchet", 30, "bold"),
    bg="#a79aab",
    activebackground="#584c5c",
    width=10,
    height=1,
)
button_submit.place(x=390, y=560)


def update_time():
    """Update current time fuction. Compare current time with set_alarm. If they are qual trigger alarm()"""
    global current_time
    current_time = strftime("%H:%M:%S")
    time.config(text=current_time)

    if current_time == set_alarm:
        print("alarm")
        alarm()
    time.after(1000, update_time)


""" Create TKinter actual time label (updated with update_time()) """
time = Label(
    window,
    font=("Trebuchet", 40, "bold"),
    bg="#a79aab",
    relief=SUNKEN,
    bd=5,
)
time.place(x=10, y=220)


""" define image for next label """
alarm_image = PhotoImage(file="data/alarm-clock_background.png")

""" Insert text on header"""
label = Label(
    window,
    text="Set time for alarm:",
    font=("Trebuchet", 40, "bold"),
    bg="#a79aab",
    relief=SUNKEN,
    bd=5,
    image=alarm_image,
    compound="left",
)
label.pack()


def clear():
    """Set command for clear spinbox to default value"""
    spinbox_default_value_hours = IntVar(window)
    spinbox_default_value_hours.set("00")
    spinbox_default_value_minutes = IntVar(window)
    spinbox_default_value_minutes.set("00")
    spinbox_default_value_seconds = IntVar(window)
    spinbox_default_value_seconds.set("00")
    scale_hours.config(textvariable=spinbox_default_value_hours)
    scale_minutes.config(textvariable=spinbox_default_value_minutes)
    scale_seconds.config(textvariable=spinbox_default_value_seconds)


""" Define clear for alarm input button """
button_clear = Button(
    window,
    text="clear",
    command=clear,
    font=("Trebuchet", 20, "bold"),
    bg="#a79aab",
    activebackground="#584c5c",
    width=22,
)
button_clear.place(x=250, y=300)


""" SET alarm time in spinbox """
scale_hours = Spinbox(
    window,
    from_=0,
    to=23,
    font=("Trebuchet", 40, "bold"),
    bg="#a79aab",
    relief=SUNKEN,
    bd=5,
    width=3,
    format="%02.0f",
    buttonbackground="#766f78",
)
scale_minutes = Spinbox(
    window,
    from_=0,
    to=59,
    font=("Trebuchet", 40, "bold"),
    bg="#a79aab",
    relief=SUNKEN,
    bd=5,
    width=3,
    format="%02.0f",
    buttonbackground="#766f78",
)
scale_seconds = Spinbox(
    window,
    from_=0,
    to=59,
    font=("Trebuchet", 40, "bold"),
    bg="#a79aab",
    relief=SUNKEN,
    bd=5,
    width=3,
    format="%02.0f",
    buttonbackground="#766f78",
)
scale_hours.place(x=250, y=220)
scale_minutes.place(x=380, y=220)
scale_seconds.place(x=510, y=220)


""" Init audio player with pygame mixer. Set alarm to ringtone"""
pygame.mixer.init()


def alarm():
    """Define ringtone for alarm with pygame"""
    sound = pygame.mixer.Sound(ringtone)
    sound.play(1)


def stop_alarm():
    """Define stop alarm fuction"""
    pygame.mixer.stop()


""" Create and Define stop alarm button """
button_stop = Button(
    window,
    text="Stop alarm",
    command=stop_alarm,
    font=("Trebuchet", 30, "bold"),
    bg="#a79aab",
    activebackground="#584c5c",
)
button_stop.place(x=10, y=560)


def update_alarm():
    """Function for update actual alarm"""
    alarm_set_to.config(text=set_alarm)
    alarm_set_to.after(1000, update_alarm)


""" Create TKinter label with actual alarm time """
info_alarm = Label(
    window,
    text="Alarm set to:",
    font=("Trebuchet", 35, "bold"),
    bg="#a79aab",
    relief=SUNKEN,
    bd=5,
)
info_alarm.place(x=10, y=400)


""" Create TKinter and define alarm set to info """
alarm_set_to = Label(
    window, font=("Trebuchet", 35, "bold"), bg="#a79aab", relief=SUNKEN, bd=5, width=10
)
alarm_set_to.place(x=330, y=400)


def clear_alarm():
    """Define Fuction for clear alarm"""
    global set_alarm
    set_alarm = ""


""" Create and define clear alarm button """
button_clear_alarm = Button(
    window,
    text="clear alarm",
    command=clear_alarm,
    font=("Trebuchet", 20, "bold"),
    bg="#a79aab",
    activebackground="#584c5c",
    width=36,
)
button_clear_alarm.place(x=10, y=475)


""" Place windows on screen, listen for events """
update_time()
update_alarm()
window.mainloop()
