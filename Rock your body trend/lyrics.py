# This code is the lyrics trend of rock your body song ! 

import sys
from rich import print
from time import sleep

print("AUTHOR: xyza.user")

def printLyrics():
    lines = [        
        ("I wanna da-", 0.08),        # The time is for the character  
        ("I wanna dance in the lights", 0.08),  
        ("I wanna ro-", 0.07),      
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),   
        ("I wanna go for a ride", 0.08),    
        ("Hop in the music and", 0.08), 
        ("Rock your body", 0.07),
        ("Rock that body", 0.06),
        ("come on, come on", 0.04),
        ("Rock that body", 0.05),
        ("(Rock your body)", 0.05),
        ("Rock that body", 0.05),
        ("come on, come on", 0.04),
        ("Rock that.... body", 0.075),
    ]

    # Adjusted delays between lines (in seconds)
    delays = [0.2, 0.8, 0.2, 0.8, 0.2, 0.7, 0.6, 0.6, 0.2, 0.15, 0.2, 0.25, 0.2, 0.2, 5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            if line == '(Rock your body)':
                print(f"[bold italic #FF0000]{char}[/bold italic #FF0000]", end='')
            else:
                print(f"[bold italic #ADD8E6]{char}[/bold italic #ADD8E6]", end='')  
            sys.stdout.flush()
            sleep(char_delay)
        print()
        if i == len(lines) - 1:
            print("[blink][bold italic #ADD8E6]🎵🎶🎵[/bold italic #ADD8E6][/blink]")
        sleep(delays[i])


if __name__ == "__main__":

    printLyrics()
