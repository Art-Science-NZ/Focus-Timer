from pathlib import Path
# Import functions
import functions.sound as sound
import functions.timer as timer

# Set Folder where you have cloned the file.  (If not in Documents then edit the below as well)
FOLDER_NAME = "Focus Timer"
print("How many minutes do you want the timer to run for?")
MINUTES = input() 

def main():
    # Set params
    play_times = 3
    # Loop through timer
    finished = False
    while not finished:
        finished = timer.run_timer(float(MINUTES))
    # Once timer is over make sound
    sound.make_sound("".join([str(Path.home()), "\\Documents\\", FOLDER_NAME, "\\Focus-Timer\\src\\static\\ring_sound.mp3"]), play_times) #Edit path if you need.
if __name__ == '__main__':
    main()