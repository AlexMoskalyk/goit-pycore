from datetime import datetime



def get_days_from_today(date:str)->int:
    input_date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.today()
    date_diff = current_date - input_date
    return date_diff.days

print(get_days_from_today('2024-11-22'))