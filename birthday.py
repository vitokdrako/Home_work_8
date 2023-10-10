from datetime import date, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = {day: [] for day in weekdays}

    for _ in range(7):
        for user in users:
           
            if today.month == user['birthday'].month and today.day > user['birthday'].day:
                continue
            if today.month > user['birthday'].month:
                continue

           
            if today.weekday() == user['birthday'].weekday():
                
                if weekdays[today.weekday()] in ['Saturday', 'Sunday']:
                    birthdays['Monday'].append(user['name'])
                else:
                    birthdays[weekdays[today.weekday()]].append(user['name'])
        today += timedelta(days=1)

   
    for day in list(birthdays.keys()):
        if not birthdays[day]:
            del birthdays[day]

    return birthdays


users = [
    {"name": "Тарас Шевченко", "birthday": date(1814, 3, 9)},
    {"name": "Леся Українка", "birthday": date(1871, 2, 25)},
    {"name": "Андрій Шептицький", "birthday": date(1865, 7, 29)},
    {"name": "Микола Лисенко", "birthday": date(1842, 3, 22)},
    {"name": "Іван Франко", "birthday": date(1856, 8, 27)},
    {"name": "Василь Симоненко", "birthday": date(1935, 1, 8)},
    {"name": "Олесь Гончар", "birthday": date(1918, 4, 3)},
    {"name": "Микола Гоголь", "birthday": date(1809, 3, 31)},
    {"name": "Володимир Винниченко", "birthday": date(1880, 7, 27)},
    {"name": "Сергій Корольов", "birthday": date(1907, 1, 12)}
]


print(get_birthdays_per_week(users))
