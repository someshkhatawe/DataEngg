import datetime

def get_week_number(date):
    # Define a custom function to get the week number starting from Wednesday
    def week_number_wednesday(date):
        year, week_num, weekday = date.isocalendar()
        if weekday == 7:  # Sunday is considered as the last day of the week in isocalendar
            weekday = 0
        return week_num, weekday

    # Calculate the week number and weekday
    week_num, _ = week_number_wednesday(date)

    return week_num

# Example usage:
date = datetime.date(2023, 10, 4)  # October 4, 2023 (a Wednesday)
week_number = get_week_number(date)
print(f"Week number: {week_number}")