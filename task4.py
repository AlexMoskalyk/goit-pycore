import datetime

def get_upcoming_birthdays(users):
    today = datetime.datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime.date(today.year, birthday.month, birthday.day)

        if birthday_this_year < today:
            birthday_this_year = datetime.date(today.year + 1, birthday.month, birthday.day)

        time_to_birthday = (birthday_this_year - today).days

        if time_to_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5:
                days_to_add = 7 - congratulation_date.weekday()
                congratulation_date += datetime.timedelta(days=days_to_add)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1990.11.17"},
    {"name": "Jane Doe", "birthday": "1995.11.20"},
    {"name": "Bob Smith", "birthday": "1980.11.25"},
    {"name": "Margo Smith", "birthday": "1980.11.29"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)