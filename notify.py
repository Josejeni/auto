
import time
from plyer import notification
 
 
if __name__=="__main__":
        while True:
    
            notification.notify(
                title = "Water",
                message="Take some water dude...." ,
            
                # displaying time
                timeout=4
    )
        # waiting time
            time.sleep(1800)