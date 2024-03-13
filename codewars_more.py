def format_duration(seconds):
    secs = seconds % 60
    mins = seconds // 60
    hours = mins // 60
    days = hours // 24
    years = days // 365

    if seconds == 0:
        return "now"
    elif seconds < 60:
        return f"{seconds} second{'s' if seconds > 1 else ''}"
    elif 60 <= seconds < 3600:
        if seconds == 0:
            return f"{mins} minute{'s' if mins > 1 else ''}"
        else:
            return f"{mins} minute{'s' if mins > 1 else ''} and {secs} second{'s' if secs > 1 else ''}"
    elif 3600 <= seconds < 86400:  # 3600 = 1 hour
        if hours >= 1 and seconds == 0 and mins == 0:
            return f"{hours} hour{'s' if hours > 1 else ''}"
        # else:
        #     return f"{hours} hour{'s' if hours > 1 else ''}, {mins} minute{'s' if mins > 1 else ''} and {secs} second{'s' if secs > 1 else ''}"

        # if seconds >= 31536000:
        #     return f"{seconds // 31536000} year{'s' if seconds // 31536000 > 1 else ''}"
        # elif seconds >= 86400:
        #     return f"{seconds // 86400} day{'s' if seconds // 86400 > 1 else ''}"
        # elif seconds >= 3600:
        #     return f"{seconds // 3600} hour{'s' if seconds // 3600 > 1 else ''}"


print(format_duration(3600))
