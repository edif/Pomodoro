import tkinter as tk
import datetime

# Create main window
root = tk.Tk()
root.title("Pomodoro Timer")

# Create Entry widgets for work and break time
work_entry = tk.Entry(root)
work_entry.pack()
break_entry = tk.Entry(root)
break_entry.pack()

# Create a label to display the time remaining
time_left = tk.Label(root, font=("Helvetica", 48))
time_left.config(text="00:00")
time_left.pack()

# Set the initial mode to "work" and the initial remaining time to the work time
mode = "work"
work_time = "25:00"
break_time = "05:00"
remaining = work_time

# Set the initial running state to False
running = False

# Function to get work and break time from Entry widgets
def configure_time():
    """
    Configure the work and break time according to the user input
    """
    global work_time
    global break_time
    global remaining
    # Convert the user input from a string in the format "MM:SS" to a datetime object
    work_time = datetime.datetime.strptime(work_entry.get(), '%M:%S')
    # Extract the minutes and seconds from the datetime object and convert to total seconds
    work_time = work_time.minute*60 + work_time.second
    break_time = datetime.datetime.strptime(break_entry.get(), '%M:%S')
    break_time = break_time.minute*60 + break_time.second
    if mode == "work":
        remaining = work_time
    else:
        remaining = break_time


# Function to start timer
def start_pomodoro():
    configure_time()
    global running
    running = True
    countdown()

# Function to pause timer
def pause_pomodoro():
    global running
    running = False
    time_left.config(text="Paused")

# Function to reset timer
def reset():
    global mode
    mode = "work"
    configure_time()
    start_pomodoro()

# Function to handle countdown
def countdown():
    global running
    global mode
    # check if the countdown is running
    if running:
        global remaining
        # check if there is still time remaining
        if remaining > 0:
            # use divmod to separate remaining time into minutes and seconds
            minutes, seconds = divmod(remaining, 60)
            # update the time_left label with the current time
            time_left.config(text="{:02}:{:02}".format(minutes, seconds))
            # decrement the remaining time by 1 second
            remaining -= 1
            # call the countdown function again after 1000 milliseconds (1 second)
            root.after(1000, countdown)
        else:
            # check if the current mode is "work"
            if mode == "work":
                # change the mode to "break"
                mode = "break"
                # update the time_left label
                time_left.config(text="Break Time")
                # configure the time for the break
                configure_time()
            else:
                # change the mode to "work"
                mode = "work"
                # update the time_left label
                time_left.config(text="Work Time")
                # configure the time for the work
                configure_time()
    else:
        # update the time_left label to "Paused"
        time_left.config(text="Paused")


# Create the "Start" button
start_button = tk.Button(root, text="Start", command=start_pomodoro)
# Pack the "Start" button to the GUI
start_button.pack()

# Create the "Pause" button
pause_button = tk.Button(root, text="Pause", command=pause_pomodoro)
# Pack the "Pause" button to the GUI
pause_button.pack()

# Create the "Reset" button
reset_button = tk.Button(root, text="Reset", command=reset)
# Pack the "Reset" button to the GUI
reset_button.pack()

# Start the main event loop of the tkinter GUI
root.mainloop()
