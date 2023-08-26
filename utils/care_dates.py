from datetime import datetime, timedelta

def get_next_care_date(last_care_date, care_frequency):

    try:
        upcoming_care_datetime = last_care_date + timedelta(days = care_frequency)

    # Convert the upcoming_care_datetime to formatted string
        next_care_date = upcoming_care_datetime.strftime('%Y-%m-%d')
        return next_care_date
    
    except TypeError:
        print("Incorrent input, must be daytime object and an int")
        return None
    
    except Exception as error:
        print("An unexpected error occurred:", error)
        return None

def is_next_care_date_up_to_date(last_care):
        assert isinstance(last_care, datetime)
        up_to_date = last_care > datetime.now()
        return up_to_date


