# **ALARM CLOCK**
### **Video Demo:**  [link](https://youtu.be/NYL2NYzlfvU)

**Description:**
Alarm clock with a graphical user interface created in Python. After starting the program, the users will see a window with the actual time updated every second. The user can enter the alarm time using the sliders for the hour, minute and second. The program has a default ringtone, but there is a button with which you can upload a customized ringtone file. After entering the alarm time, the user needs to approve it with the set alarm button. When the sound starts, you can turn it off with the "stop alarm" button. There are two other buttons for clearing the alarm before it rings and clear input time on sliders.

The program consists of seven functions, and its implemented with a Tkinter module for GUI, pygame for playing sounds. The **upload_mp3()** changes the default alarm ringtone for upload one, and the user can choose a different file with a file dialog window. The **set_alarm_time()** function retrieves data from user input in the slider and returns a variable for the alarm time. The **update_time()** is a recursive function that listens for alarms and sets the current time as a global variable, and updates every second. The **Clear()** introduces default values ​​for sliders. Their scale is fixed from 0 to 23 for hours, 0 to 59 for minutes and seconds. The **alarm()** and **stop_alarm()** functions are responsible for starting and stopping the sound with pygame library. The **update_alarm()** sets the global variable for alarm, and **clear_alarm()** removes it. All visible elements were created with Tkinter.

The goal of this project was to learn some new skills connected with Python and GUI. That's why I chose this Tkinter module, which created an exciting project for me, and allowed me to expand my Python knowledge in conjunction with the GUI. Microsoft Windows does not have an alarm clock by default, and in my opinion, this application, in combination with the, calendar can be helpful for many users


### Project file list description:

    alarm_clock.py - program file
    README.md - project documentation for projct
    alarm-clock_background.png - alarm clock image for GUI
    alarm-clock.png - alarm block icon for GUI
    ringtone.mp3 - default rington
