import os
import datetime
import pygame

# Clear the screen
os.system("cls" if os.name == "nt" else "clear")

# Set the alarm time
alarmH = int(input("What hour do you want the alarm to ring? "))
alarmM = int(input("What minute do you want the alarm to ring? "))
amPm = input("AM or PM? ").lower()
os.system("cls" if os.name == "nt" else "clear")

print("Waiting for alarm at {}:{}".format(alarmH, alarmM))

if amPm == "pm":
    alarmH = (alarmH + 12) % 24

while True:
    now = datetime.datetime.now()
    
    if now.hour == alarmH and now.minute == alarmM:
        print("Time to wake up")
        
        # Initialize pygame
        pygame.init()

        # Load the sound file
        pygame.mixer.music.load("C:\\Users\\Hunter Hanson\\Desktop\\Random python projects\\NWS ALarm Sound.mp3")

        # Play the sound
        pygame.mixer.music.play()

        # Keep the program running while the sound plays
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        break
