import random
import uuid
import json
import time
from random import gauss

TOTAL_RECORDS = 100000
COLORS = ["blue","magenta", "red", "yellow", "green", "cyan"]

def generate(n):
    l = []
    ctime = int(round(time.time() * 1000))
    for i in range(n):
        ctime = ctime + random.randrange(300)
        l.append(json.dumps({
            "color": random.choice(COLORS), 
            "timestamp": ctime, 
            "id": str(uuid.uuid4()), 
            "value": gauss(35,30)
            }))

i = 0
prefix = os.argv[3]
while True:
    l = generate(os.argv[2])
    with open(prefix + "/data_" + str(i))as f:
        for event in l:
            f.write(event + "\n")
    time.sleep(os.argv[1])

