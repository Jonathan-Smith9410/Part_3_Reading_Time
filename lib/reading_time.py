def reading_time(text):
    if len(text) == 0:
        return "No text present"
    calc_time = round(((len(text.split())) / 200), 1)
    return f"Your text will take {calc_time} minute/s to read"