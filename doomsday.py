import requests
import datetime
import calendar

question_num="10"

url="https://www.random.org/calendar-dates/?num="\
    + question_num\
    + "&start_day=1&start_month=1&start_year=1800"\
    "&end_day=31&end_month=12&end_year=2199&mondays=on&tuesdays=on&wednesdays=on"\
    "&thursdays=on&fridays=on&saturdays=on&sundays=on"\
    "&display=2&format=plain&rnd=new"

response=requests.get(url)

correct=0

if response.ok:
    for i in response.iter_lines():
        date = datetime.datetime.strptime(i.decode("utf-8"), "%Y-%m-%d")
        answer = input("\033[1m"+date.strftime("%Y %B %d")+"\n\033[0m")
        dayname = calendar.day_name[date.weekday()]
        if answer.lower() == dayname.lower():
            print('good job')
            correct += 1
        else:
            print('wrong, it was '+dayname+".")

print("Your score: "+str(correct)+"/"+question_num)
        
