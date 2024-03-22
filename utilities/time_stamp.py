from datetime import datetime

current_time = datetime.now()
time_with_format = current_time.strftime('%b %d, %Y')

print(time_with_format)