from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y %H:%M:%S")
#print("date and time:",date_time)

var = "15.55|65.55" 
#print(var)
values:list[str] = var.split("|")

print(f'\033[31m{values[0]}\t\t {values[1]}\t\t {date_time}\t\t \033[0m')
print("\n")

