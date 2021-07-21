def AnalogDigi(fulltime):
    'this function changes the input from am/pm to digital format or from digital format back to am/pm format'
    time = fulltime.split(' ')[0]
    try:
        AMPM = fulltime.split(' ')[1]
    except IndexError:  # am/pm format
        hour, minute = int(time.split(':')[0]), time.split(':')[1]
        minute = minute.zfill(2)  # add leading zero's
        if hour >= 12:
            hour -= 12
            if hour == 0:
                hour = 12
            return f'{hour}:{minute} PM'
        else:
            if hour == 0:
                hour = 12
            return f'{hour}:{minute} AM'
    hour, minute = int(time.split(':')[0]), time.split(':')[1]
    minute = minute.zfill(2) # add leading zero's
    if AMPM == 'PM':  # digital format > 12:59
        hour += 12
        return f'{hour}:{minute}'
    else:  # digital format < 12:59
        return f'{hour}:{minute}'

def add_week_days(startDay, nDays):
    '''this function returns the  day of the week after adding n days '''
    weekDays = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday'}
    for key in weekDays:
        if weekDays[key] == startDay.lower():
            startDayNum = key
            break
    if (startDayNum + nDays) == 7:
        return weekDays[(startDayNum + nDays)].capitalize()  # if it is the 7th day..
    elif (startDayNum + nDays) % 7 == 0:
        return startDay.lower().capitalize()  # same day as start day, dividable by 7
    else:
        return weekDays[(startDayNum + nDays) % 7].capitalize()  # not dividable by 7,


def add_time(start, duration, startDay=None):
    days = 0
    digiTime = AnalogDigi(start)
    srtHour, srtMinute = int(digiTime.split(':')[0]), int(digiTime.split(':')[1])
    durHour, durMinute = int(duration.split(':')[0]), int(duration.split(':')[1])
    if srtMinute + durMinute >= 60:
        srtHour += 1  # calculates the amount of whole hours, 60 min == 1 hour
        srtMinute = (srtMinute + durMinute) - 60  # adds the leftover minutes
    else:
        srtMinute += durMinute
    if srtHour + durHour >= 24:
        days = int((srtHour + durHour) / 24)  # calculates the amount of whole days, 24hour == 1 day
        srtHour = (srtHour + durHour) % 24  # adds the leftover hours of the division
    else:
        srtHour += durHour
    analogTime = AnalogDigi(f'{srtHour}:{srtMinute}')
    if startDay: # if the startday var is specified..
        weekday = add_week_days(startDay, days) # calculate the weekday
        if days == 0:
            return f'{analogTime}, {weekday}'
        elif days == 1:
            return f'{analogTime}, {weekday} (next day)'
        else:
            return f'{analogTime}, {weekday} ({days} days later)'
    else:
        if days == 0:
            return analogTime
        elif days == 1:
            return f'{analogTime} (next day)'
        else:
            return f'{analogTime} ({days} days later)'