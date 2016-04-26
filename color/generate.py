import random
import uuid
import json
import time
from random import gauss

TOTAL_RECORDS = 100000
COLORS = ["blue","magenta", "red", "yellow", "green", "cyan"]
BASETIME=int(round(time.time() * 1000))

ctime = BASETIME
for i in range(TOTAL_RECORDS):
    ctime = ctime + random.randrange(300)
    print(json.dumps({"color": random.choice(COLORS), "timestamp": ctime, "id": str(uuid.uuid4()), "value": gauss(42,30)}))
