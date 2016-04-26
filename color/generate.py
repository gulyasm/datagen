import random
import uuid
import json
import time
from random import gauss
import sys

TOTAL_RECORDS = 100000
COLORS = ["blue","magenta", "red", "yellow", "green", "cyan"]

def generate(n):
    l = []
    ctime = int(round(time.time() * 1000))
    for x in range(n):
        ctime = ctime + random.randrange(300)
        l.append(json.dumps({
            "color": random.choice(COLORS), 
            "timestamp": ctime, 
            "id": str(uuid.uuid4()), 
            "value": gauss(35,30)
            }))
    return l

i = 0
prefix = sys.argv[3]
backoff = int(sys.argv[1])
events = int(sys.argv[2])

while True:
    l = generate(events)
    with open(prefix + "/data_" + str(i), "w") as f:
        for event in l:
            f.write(event + "\n")
    i += 1
    time.sleep(backoff)

