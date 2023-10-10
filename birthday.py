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
    {"name": "Bill Gates", "birthday": date(1955, 10, 12)},
    {"name": "Steve Jobs", "birthday": date(1955, 2, 24)}
]

print(get_birthdays_per_week(users))
