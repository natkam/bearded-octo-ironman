import sys
import datetime


def countdown(to_what):
    now = datetime.datetime.now()
    target = datetime.datetime.strptime(to_what, "%Y-%m-%d %H:%M:%S")
    left = target - now
    total_seconds = left.seconds
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time_left = "{day}d {hour}h {minute}m {second}s".format(day=left.days,
                hour=hours, minute=minutes, second=seconds)
    return """now: {time_now:>22}\ntarget: {time_target}\nleft: {time_left:>14}""".format(
            time_now=now.strftime("%Y-%m-%d %H:%M:%S"),
            time_target=target, time_left=time_left)

if __name__ == '__main__':
    print(countdown(sys.argv[1]))
