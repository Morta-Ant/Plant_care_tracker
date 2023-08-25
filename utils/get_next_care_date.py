from datetime import datetime, timedelta

def get_next_care_date(last_care_date, care_frequency):

    try:
    # Calculate the upcoming care date by adding care_frequency days to last_care_datetime
        upcoming_care_datetime = last_care_date + timedelta(days = care_frequency)

    # Convert the upcoming_care_datetime to formatted string
        next_care_date = upcoming_care_datetime.strftime('%Y-%m-%d')
        return next_care_date
    
    except ValueError :
        print("The provided date format is incorrect. Please use the format 'YYYY-MM-DD HH:MM:SS'")
        return None
    
    except Exception as error:
        print("An unexpected error occurred:", error)
        return None

def is_next_care_date_up_to_date(last_care):
        up_to_date = last_care > datetime.now()
        return up_to_date
