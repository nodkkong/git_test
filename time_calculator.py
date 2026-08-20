def add_time(start, duration, day=""):
    days = {
    "":"",
    "Sunday" : 1,
    "Monday" : 2,
    "Tuesday" : 3,
    "Wednesday" : 4,
    "Thursday" : 5,
    "Friday" : 6,
    "Saturday" : 7
    }  
    
    # Start parsing
    time_part, ampm = start.split()
    hour, minute = map(int, time_part.split(':'))
    
    # Convert start time to minutes
    start_minutes = hour % 12 * 60 + minute
    if ampm == "PM":
        start_minutes += 12 * 60
    
    # Duration parsing
    dur_hour, dur_min = map(int, duration.split(':'))
    duration_minutes = dur_hour * 60 + dur_min

    # Total minutes and calculate new time
    total_minutes = start_minutes + duration_minutes
    total_days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    
    new_hour_24 = remaining_minutes // 60
    new_minute = remaining_minutes % 60
    
    new_ampm = "AM" if new_hour_24 < 12 else "PM"
    new_hour = new_hour_24 % 12
    if new_hour == 0:
        new_hour = 12
        
    # Day of week
    if day:
        day_index = (days[day.capitalize()] + total_days - 1) % 7 + 1
        for key, value in days.items():
            if value == day_index:
                new_day = key
                break
        day_part = f", {new_day}"
    else:
        day_part = ""
    
    # Days later messge
    if total_days == 0:
        days_later_msg = ""
    elif total_days == 1:
        days_later_msg = " (next day)"
    else:
        days_later_msg = f" ({total_days} days later)"

    return f"{new_hour}:{new_minute:02d} {new_ampm}{day_part}{days_later_msg}"