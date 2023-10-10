from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    today = date.today()
    result = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}
    
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = user["birthday"].replace(year=today.year + 1)
        delta = (birthday_this_year - today).days
        
        if delta <= 6:
            if birthday_this_year.weekday() == 5: 
                result["Monday"].append(user["name"])
            elif birthday_this_year.weekday() == 6: 
                result["Monday"].append(user["name"])
            else:
                day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][birthday_this_year.weekday()]
                result[day_name].append(user["name"])
    
    result = {k: v for k, v in result.items() if v}
    
    return result

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 24).date()},
        {"name": "Andriy Shevchenko", "birthday": datetime(1976, 9, 29).date()},
        {"name": "Milla Jovovich", "birthday": datetime(1975, 12, 17).date()},
        {"name": "Max Levchin", "birthday": datetime(1975, 7, 11).date()},
        {"name": "Taras Shevchenko", "birthday": datetime(1814, 3, 9).date()},
        {"name": "Ivan Franko", "birthday": datetime(1856, 8, 27).date()},
        {"name": "Olena Teliha", "birthday": datetime(1906, 7, 21).date()},
        {"name": "Mykhailo Hrushevsky", "birthday": datetime(1866, 9, 29).date()},
        {"name": "Lesya Ukrainka", "birthday": datetime(1871, 2, 25).date()},
        {"name": "Klitschko Wladimir", "birthday": datetime(1976, 3, 25).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
