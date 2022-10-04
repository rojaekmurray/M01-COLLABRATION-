import multiprocessing
from random import random
from datetime import datetime
from time import sleep
def three_times(seconds): 
  sleep(seconds)    
  print(f"Waiting {round(seconds, 2)} seconds. The current time is {datetime.utcnow()}.")
if __name__ == '__main__':
  for n in range(3): 
    seconds = random()  
    app = multiprocessing.Process(target=three_times, args=(seconds,))   
    app.start()
