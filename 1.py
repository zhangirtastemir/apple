def format_duration(seconds):
    minute = seconds % 60
    hour = seconds % 3600

    minute1 = (seconds - (seconds // 3600) * 3600) // 60
    seconds1 = (seconds - (seconds // 3600) * 3600) - ((seconds - (seconds // 3600) * 3600) // 60) * 60
    minute2 = (str(minute1) + " " + "minute" if minute1 != 0 else "")
    seconds2 = (str(seconds1) + " " + "seconds" if seconds1 != 0 else "")

    hour1 = (seconds - ((seconds // 3600) // 24) * 86400) // 3600
    hour2 = (str(hour1) + ' ' + 'hour' if hour1 != 0 else '')

    return hour2 + " " + minute2 + " " + seconds2


print(format_duration(int(input())))