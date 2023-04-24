from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    today = datetime.now().date()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today_weekday = today.weekday()
    monday = today - timedelta(days=today_weekday)
    sunday = monday + timedelta(days=6)
    birthday_dict = {}

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        if monday <= birthday <= sunday:
            birthday_weekday = weekdays[birthday.weekday()]
            if birthday_weekday in birthday_dict:
                birthday_dict[birthday_weekday].append(name)
            else:
                birthday_dict[birthday_weekday] = [name]

    for weekday in weekdays[:5]:
        if weekday in birthday_dict:
            names = ', '.join(birthday_dict[weekday])
            print(f"{weekday}: {names}")

    if 'Saturday' in birthday_dict or 'Sunday' in birthday_dict:
        names = []
        if 'Saturday' in birthday_dict:
            names.extend(birthday_dict['Saturday'])
        if 'Sunday' in birthday_dict:
            names.extend(birthday_dict['Sunday'])
        monday_names = ', '.join(names)
        print(f"Monday: {monday_names}")


if __name__ == '__main__':

    users = [
        {'name': 'Dave', 'birthday': datetime(1979, 4, 30)},
        {'name': 'Eve', 'birthday': datetime(1991, 5, 1)},
        {'name': 'Ali', 'birthday': datetime(2001, 4, 24)},
        {'name': 'Bob', 'birthday': datetime(1992, 4, 25)},
        {'name': 'Lee', 'birthday': datetime(1985, 4, 27)},
        {'name': 'Frank', 'birthday': datetime(1992, 5, 2)},
        {'name': 'Maria', 'birthday': datetime(1980, 5, 3)}
    ]
    
    get_birthdays_per_week(users)