import sys, datetime
from datetime import timedelta

target = datetime.datetime.strptime(sys.argv[1] , '%Y-%m-%d %H:%M:%S')
now = datetime.datetime.now()

diff = target - now
days = diff.days
minutes, seconds = divmod(diff.seconds, 60)
hours, minutes = divmod(minutes, 60)

now = str(now)[:19]
print("now:    {0}".format(now))
print("target: {0}".format(target))
print("left:   {0}d {1}h {2}m {3}s".format(days, hours, minutes, seconds))
