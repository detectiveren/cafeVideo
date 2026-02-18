from datetime import datetime


def time_ago(timestamp):
    if not isinstance(timestamp, int):
        timestamp = int(timestamp)
    now = datetime.now()
    current_datetime = datetime.fromtimestamp(timestamp)

    # Calculate the time difference between when the video was uploaded and now
    time_diff = now - current_datetime
    seconds = time_diff.total_seconds()

    # Turn it into a readable format
    if seconds >= 0:
        if seconds < 60:
            result = f"{int(seconds)} seconds ago"
        elif seconds < 3600:
            minutes = seconds // 60
            result = f"{int(minutes)} minute{'s' if minutes > 1 else ''} ago"
        elif seconds < 86400:
            hours = seconds // 3600
            result = f"{int(hours)} hour{'s' if hours > 1 else ''} ago"
        elif seconds < 604800:
            days = seconds // 86400
            result = f"{int(days)} day{'s' if days > 1 else ''} ago"
        elif seconds < 2629800:
            weeks = seconds // 604800
            result = f"{int(weeks)} week{'s' if weeks > 1 else ''} ago"
        elif seconds < 31557600:
            months = seconds // 2629800
            result = f"{int(months)} month{'s' if months > 1 else ''} ago"
        else:
            years = seconds // 31557600
            result = f"{int(years)} year{'s' if years > 1 else ''} ago"

        return result
    else:
        if seconds > -60:
            result = f"In {int(seconds)} seconds"
        elif seconds > -3600:
            minutes = (-seconds) // 60
            result = f"In {int(minutes)} minutes"
        elif seconds > -86400:
            hours = (-seconds) // 3600
            result = f"In {int(hours)} hours"
        elif seconds > -604800:
            days = (-seconds) // 86400
            result = f"In {int(days)} days"
        elif seconds > -2419200:
            weeks = (-seconds) // 604800
            result = f"In {int(weeks)} weeks"
        elif seconds > -29030400:
            months = (-seconds) // 2419200
            result = f"In {int(months)} months"
        else:
            years = (-seconds) // 31557600
            result = f"In {int(years)} years"

        return result


def getVideoDatetime(timestamp):
    if not isinstance(timestamp, int):
        timestamp = int(timestamp)
    current_datetime = datetime.fromtimestamp(timestamp)
    videoUploadDate = str(current_datetime.strftime("%B %d, %Y"))

    return videoUploadDate
