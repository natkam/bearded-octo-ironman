import sys
from datetime import datetime, timedelta

target = datetime.strptime(sys.argv[1], "%Y-%m-%d %H:%M:%S")
now = datetime.now()
left = target - now # type(left) -> timedelta

secs = left.total_seconds()
mins, secs = divmod(secs, 60)
hrs, mins = divmod(mins, 60)
days, hrs = divmod(hrs, 24)

answer = "{}d {}h {}m {}s".format(int(days), int(hrs), int(mins), int(secs))
str_now = now.strftime("%Y-%m-%d %H:%M:%S")

print("now: ".ljust(8), str_now)
print("target: ", target)
print("left: ".ljust(8), answer)
