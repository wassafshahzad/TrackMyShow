import time
import threading
import time
from scraper import get_latest_episode
from win10toast import ToastNotifier
toaster = ToastNotifier()

def exit_on_keypress(e,user):

    while not e.isSet(): 
        print("Working... ", flush=True)
        user.notify(get_latest_episode(user.show.link),toaster,"Hello there")
        time.sleep(3)


def init(user):
    print("You can press CTRL+C to exit anytime ")
    e = threading.Event()
    th = threading.Thread(target=exit_on_keypress,daemon=True,args=(e,user))
    th.start()
    while th.isAlive():
        try: time.sleep(1) #wait 1 second, then go back and ask if thread is still alive
        except KeyboardInterrupt: 
            e.set() 
            th.join() #wait for the thread to finish 

