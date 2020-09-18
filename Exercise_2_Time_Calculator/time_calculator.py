def add_time(start, duration, day=None):
  
  #start time split (hour,min,period)
  time,period = start.split()
  start_hour,start_minute = time.split(':')
  start_period = period
  new_time = 0

  #duration split
  duration_hour,duration_minute = duration.split(':')  
  day_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  end_hour = int(start_hour) + int(duration_hour)
  end_minute = int(start_minute) + int(duration_minute)    
  
  #hours
  if end_minute > 59:
    end_minute %= 60
    end_hour += 1 
  end_hour_period = end_hour  
  while end_hour > 12:
    end_hour -= 12
  
  #periods
  duration_periods = 0    
  while end_hour_period > 11:
    end_hour_period -= 12
    period = "PM" if period == "AM" else "AM"
    duration_periods += 1
  if duration_periods %2 != 0:
    if start_period == "PM":
      duration_periods += 1
    else:
      duration_periods -= 1
  
  new_time = f"{end_hour}:{str(end_minute).zfill(2)} {period}"
  
  #If the function is given the optional starting day of the week parameter
  duration_days = 0
  duration_days = duration_periods / 2

  if day:
    day_index = day_list.index(day.title())
    new_day_index = int((day_index + duration_days) % 7)
    new_time += f", {day_list[new_day_index]}" 

  if duration_days == 1:
    new_time += " (next day)"

  if duration_days > 1:
    new_time += f" ({int(duration_days)} days later)"

  return new_time