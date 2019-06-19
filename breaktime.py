import time
import webbrowser
totalbreaks = 3
breakcount = 0

while breakcount < totalbreaks:
    time.sleep(2*60*60)
    webbrowser.open('https://www.youtube.com')
    breakcount += 1
