import sys
from datetime import datetime


date_format = "%Y-%m-%d %H:%M:%S"


def format_timedelta(delta):
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "%dd %dh %dm %ds" % (days, hours, minutes, seconds)


target_print = sys.argv[1]
target = datetime.strptime(target_print, date_format)
present = datetime.now()
present_print = present.strftime(date_format)
left_print = format_timedelta(target - present)

print("\nnow:\t" + present_print)
print("target:\t" + target_print)
print("left:\t" + left_print + "\n")