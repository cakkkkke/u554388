from datetime import datetime

def date_passed(todays_date, scheduled_date):
    todays_date = todays_date.replace('th', '')
    scheduled_date = scheduled_date.replace('th', '')
    date_format_input=('%d %B')
    date_today = datetime.strptime(todays_date,date_format_input)
    date_scheduled = datetime.strptime(scheduled_date,date_format_input)

    if date_today < date_scheduled:
        print(f'the schedule date have not passed ')
    elif date_today > date_scheduled:
        print(f'the schedule date has passed ')
    else:
        print(f'the schedule date is today')




# Test cases

date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
