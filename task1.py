from datetime import datetime



def get_days_from_today(date):
    # Convert the input date string to a datetime object
    input_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Get the current date
    current_date = datetime.today()
    
    # Calculate the difference between the current date and the input date
    date_diff = current_date - input_date
    
    # Return the difference in days as an integer
    return date_diff.days

print(get_days_from_today('2024-11-22'))