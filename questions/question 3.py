from datetime import datetime

date = datetime.now()
formatted_date = date.strftime("%Y-%m-%d %I:%M:%S %p")
print(formatted_date)