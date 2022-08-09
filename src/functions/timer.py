import time
import datetime
import os

# Create class that acts as a countdown
def run_timer(minutes):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Calculate the total number of seconds
    total_seconds = minutes * 60
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        # Prints the time left on the timer
        print(timer, end="\r")
        # Delays the program one second
        time.sleep(1)
        # Reduces total time by one second
        total_seconds -= 1
    timer = datetime.timedelta(seconds = 0)
    print(timer, end="\r")
    return True
 
