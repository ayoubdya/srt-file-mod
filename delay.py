from datetime import datetime,timedelta
import re

FILE = input("input file path : ")
DELAY = int(input("input the delay : "))

with open(FILE, 'r', encoding="utf8") as f:
    str = f.read()

timeStamps = re.findall(r'\d{2}:\d{2}:\d{2},\d{3}', str)

for time in timeStamps:
    time1 = datetime.strptime(time, "%H:%M:%S,%f") + timedelta(seconds=DELAY)
    time2 = time1.strftime("%H:%M:%S,%f")[:-3]
    str = re.sub(time, time2, str)
    
with open(FILE[:-4]+'_delay.srt', 'w', encoding="utf8") as f:
    f.write(str)
