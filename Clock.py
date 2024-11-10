import datetime as dt
import time
import os
while True:
    now = dt.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_time2= now.strftime("%H:%M:%S")
    current_time3= now.strftime("%B %d, %Y")
    print(current_time)
    print(current_time2)
    print(current_time3)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')