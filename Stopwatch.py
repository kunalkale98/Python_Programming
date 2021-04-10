#Author: Kunal Kale
#Date: 09/04/2021
#Description: Stopwatch Program for measuring the time that elapses between the start and end clicks

import logs
import time

#Logger is defined to create error logs of the program
logger = logs.set_logger()

#Function for getting the elapsed time
def stopwatch(seconds):        
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    hours = int(minutes // 60)
    minutes = int(minutes % 60)
    logger.info(f"{hours}:{minutes}:{seconds}")

#Function to start and end the stopwatch 
def control():
    try:
        input("Press Enter to Start")
        start = time.time()
    except Exception:
        logger.error("Error!,Something went wrong")
    else:
        input("Press Enter to End")
    end = time.time()
    seconds = end - start
    return seconds

#Driver Class
seconds = control()
stopwatch(seconds)
