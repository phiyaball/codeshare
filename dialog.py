#!/usr/bin/python3

import threading
import time
import itertools
import sys

# Character select
def charselect():
    print("\n 1. Chrona - Master of time, you can transport yourself to any time period", "\n 2. Timmy - Time worm, you have 3 lives", "\n 3. Clockman, a Watch maker, you recieve one hint per game")

#greeting message


# Animation for reigstration, found this on the internet and modified it for this app


done = False
# Animation for reigstration, found this on the internet and modified it for this app
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r.... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True

done = True