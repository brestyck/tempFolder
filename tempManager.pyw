import os
import datetime
import time

TEMP = r"C:/Programezz/temp/"
TEMPFILE = TEMP+"temp.py"
CONFIG = TEMP+"allowed.config"
TIMESTAMP = TEMP+"tempMetadata.time"
HOURSTODELETE = 8
ALLOWED = []

def empty():
    if os.path.exists(CONFIG):
        ALLOWED = [i.strip() for i in open(CONFIG).readlines()]
    else:
        open(CONFIG, "w").write("# This is a file of allowed exceptions (each line used as a filename, not full path)\ntempManager.pyw")
        
    
    for i in os.listdir(TEMP):
        print(i)
        if i not in ALLOWED:
            print(f"Removing {i}...")
            try:
                os.remove(TEMP+i)
            except PermissionError: pass
    deltime = datetime.datetime.now().strftime("%H:%M")
    open(TEMPFILE, "w").write(f"# Warning! This file is temporary and will be deleted 8 hrs after {deltime}\n\n\n")
    open(TIMESTAMP, "w").write(str(time.time()))

def inquire_time():
    try:
        old_time = float(open(TIMESTAMP).read())
    except FileNotFoundError:
        old_time = 0
    delta = time.time() - old_time
    if delta > 60*60*HOURSTODELETE: empty()

while True:
    inquire_time()
    time.sleep(30)
