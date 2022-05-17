import requests
import datetime
import calendar
import random
import time

question_num="10"

url="https://www.random.org/calendar-dates/?num="\
    + question_num\
    + "&start_day=1&start_month=1&start_year=1800"\
    "&end_day=31&end_month=12&end_year=2199&mondays=on&tuesdays=on&wednesdays=on"\
    "&thursdays=on&fridays=on&saturdays=on&sundays=on"\
    "&display=2&format=plain&rnd=new"

try:
    response=requests.get(url)
except:
    response=False

correct=0
times=[]
dayname=""


def ask(x):
    date = datetime.datetime.strptime(x, "%Y-%m-%d")
    start_time = time.time()
    answer = input("\033[1m"+date.strftime("%Y %B %d")+"\n\033[0m")
    times.append(time.time()-start_time)
    dayname = calendar.day_name[date.weekday()]
    if answer.lower() == dayname.lower():
        print('good job')
    else:
        print('wrong, it was '+dayname+".")
    return answer.lower() == dayname.lower()

if response.ok and response:
    for i in response.iter_lines():
        if ask(i.decode("utf-8")):
            correct += 1
            
else:
    file = open("dates", "r")
    dates=file.readlines()
    print('returned bad, opening backup file (not random)')
    for i in range(int(question_num)):
        if ask(dates[random.randint(0,len(dates))].strip('\n')):
            correct += 1

print("Your score: "+str(correct)+"/"+question_num)
print("Your average time was: "+str(sum(times)/len(times))+".")
        
